import allure


class StringRequester:
    def __init__(self, requester):
        self.__endpoint = 'object/'
        self.__requester = requester

    def get_strings(self):
        with allure.step("Получения списка строк"):
            return self.__requester.get_request(f"{self.__endpoint}string")

    def get_string(self, id):
        with allure.step(f"Получения строки {id=}"):
            return self.__requester.get_request(f"{self.__endpoint}string/{id}")

    def post_strings(self, data):
        return self.__requester.post_request(f"{self.__endpoint}string", data=data)
