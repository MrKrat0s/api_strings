import allure


class StringRequester:
    def __init__(self, requester):
        self.endpoint = 'object/'
        self.requester = requester

    def get_strings(self):
        with allure.step("Получения списка строк"):
            return self.requester.get_request(f"{self.endpoint}string")

    def get_string(self, id):
        with allure.step(f"Получения строки {id=}"):
            return self.requester.get_request(f"{self.endpoint}string/{id}")

    def post_strings(self, data):
        return self.requester.post_request(f"{self.endpoint}string", data=data)
