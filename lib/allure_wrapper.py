import allure

from lib.requester import RequesterAPI


class AllureWrapper(RequesterAPI):
    def __init__(
        self,
        hostname,
    ):
        super().__init__(hostname)

    def get_request(self, path):
        with allure.step(f"GET: {path}"):
            response = super().get_request(path=path)
            with allure.step(f"Response: {response}"):
                return response

    def post_request(self, path, data=None):
        with allure.step(f"POST: {path} | Data: {data}"):
            response = super().post_request(path=path, data=data)
            with allure.step(f"Response: {response}"):
                return response
