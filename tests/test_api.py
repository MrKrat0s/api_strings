import allure
import pytest
import uuid

from elements.handlers.string_handlers import StringRequester
from elements.schemes.string_scheme import StringScheme
from lib.tools import is_palindrome, is_valid_uuid
from lib.json_tools import JsonTools as json
from lib.allure_wrapper import AllureWrapper


@pytest.fixture(scope='class')
def requester(hostname):
    return AllureWrapper(hostname)


@pytest.fixture(scope='class')
def requester_string(requester):
    return StringRequester(requester)


@pytest.fixture
def prepare_string(requester_string, palindrome):
    status_code, response = json.prepare_answer(requester_string.post_strings(json.make_json(palindrome=palindrome)))
    with allure.step('ОР: status_code = 200'):
        assert status_code == 200

    return  response["id"], response["result"]


@allure.feature('Тесты STRING')
class TestStrings:
    @pytest.mark.parametrize("palindrome", [True, False])
    @allure.story('Создание строки')
    def test_create_string(self, requester_string, palindrome):
        allure.dynamic.title(f'{palindrome=}')

        with allure.step('Создать строку'):
            response = requester_string.post_strings(json.make_json(palindrome=palindrome))
            status_code, json_response = json.prepare_answer(response)

        with allure.step('ОР: status_code = 200'):
            assert status_code == 200

        with allure.step('ОР: схема json верна'):
            assert json.check_json_scheme(json_response, StringScheme.scheme_post_string)

        string, id = json_response["result"], json_response["id"]

        with allure.step('ОР: uuid созданой строки валиден'):
            assert is_valid_uuid(id)

        with allure.step(f'ОР: строка {'' if palindrome else 'не'} является палиндромом'):
            if palindrome:
                assert is_palindrome(string)
            else:
                assert not is_palindrome(string)

    @pytest.mark.parametrize("palindrome", ['', None, 123, 'test_stings'])
    @allure.story('Создание строки')
    def test_create_string_negative(self, requester_string, palindrome):
        allure.dynamic.title(f'Невалидный {palindrome=}')

        with allure.step('Создать строку'):
            response = requester_string.post_strings(json.make_json(palindrome=palindrome))
            status_code, json_response = json.prepare_answer(response)

        with allure.step('ОР: status_code = 400'):
            assert status_code == 400

        with allure.step(f'ОР: Wrong param "palindrome"'):
            assert json_response == json.make_json(error='Wrong param "palindrome"')

    @pytest.mark.parametrize("palindrome", [True, False])
    @allure.story('Запрос строки')
    def test_get_string(self, requester_string, prepare_string, palindrome):
        allure.dynamic.title(f'{palindrome=}')
        id_string, expected_string = prepare_string

        with allure.step(f'Запросить строку с uuid: {id_string=}'):
            response = requester_string.get_string(id=id_string)
            status_code, json_response = json.prepare_answer(response)

        with allure.step('ОР: status_code = 200'):
            assert status_code == 200

        with allure.step('ОР: схема json верна'):
            assert json.check_json_scheme(json_response, StringScheme.scheme_get_string)

        with allure.step(f'ОР: ожидаемая строка: error=Not Found'):
            assert json_response["result"] == expected_string

    @pytest.mark.parametrize("uuid",
                             [
                                 '',
                                 '123',
                                 123,
                                 str(uuid.uuid1()),
                                 str(uuid.uuid3(uuid.NAMESPACE_DNS, 'google.com')),
                                 str(uuid.uuid4()),
                                 str(uuid.uuid5(uuid.NAMESPACE_URL, 'yandex.ru')),
                             ]
                             )
    @allure.story('Запрос строки')
    def test_get_string_negative(self, requester_string, uuid):
        allure.dynamic.title(f'Невалидный {uuid=}')
        with allure.step(f'Запросить строку с uuid: {uuid=}'):
            response = requester_string.get_string(id=uuid)
            status_code, json_response = json.prepare_answer(response)

        if is_valid_uuid(uuid):
            with allure.step('ОР: status_code = 404'):
                assert status_code == 404

            with allure.step(f'ОР: ожидаемая строка: error=String not found'):
                assert json_response == json.make_json(error='String not found')
        elif uuid == "":
            with allure.step('ОР: status_code = 405'):
                assert status_code == 405

            with allure.step(f'ОР: ожидаемая строка: detail=Method Not Allowed'):
                assert json_response == json.make_json(detail='Method Not Allowed')
        else:
            with allure.step('ОР: status_code = 400'):
                assert status_code == 400

            with allure.step(f'ОР: ожидаемая строка: error=Invalide UUID'):
                assert json_response == json.make_json(error='Invalide UUID')
