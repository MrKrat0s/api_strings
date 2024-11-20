import allure

from lib.allure_wrapper import AllureWrapper


class StringRequester(AllureWrapper):
    def __init__(self, hostname):
        super().__init__(hostname, endpoint='object')

    def get_strings(self):
        with allure.step("Получения списка строк"):
            return self.get_request("string")

    def get_string(self, id):
        with allure.step(f"Получения строки {id=}"):
            return self.get_request(f"string/{id}")

    def post_strings(self, data):
        return self.post_request("string", data=data)

    scheme_get_string = {
        "type": "object",
        "properties": {
            "result": {"type": "string"},
        },
        "required": ["result"]
    }