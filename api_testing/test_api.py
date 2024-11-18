import pytest
from string_handlers import StringRequester
from lib import Tools
from uuid import UUID


@pytest.fixture(scope='class')
def requester_string():
    return StringRequester()


class TestStrings:
    @pytest.mark.parametrize("palindrome", [True, False])
    def test_string(self, requester_string, palindrome):
        # Отправляем POST запрос создаем строку
        response_post = requester_string.post_strings(Tools.make_json(palindrome=palindrome))
        string = response_post["result"]
        id = response_post["id"]

        # Проверяем валидность uuid
        assert Tools.is_valid_uuid(id)

        # Проверяем в зависимости от параметризации, верно ли сгенерированна строка
        if palindrome:
            assert Tools.is_palindrome(string)
        else:
            assert not Tools.is_palindrome(string)

        # Отправляем get запрос с созданным id
        response_get = requester_string.get_string(id=id)

        # Проверяем правильность полученной строки
        assert response_get['result'] == string