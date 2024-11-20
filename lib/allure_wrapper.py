import allure

from lib.requester import RequesterAPI


class AllureWrapper(RequesterAPI):
    def __init__(
        self,
        hostname,
        endpoint="",
    ):
        super().__init__(hostname, endpoint)

    def get_request(self, path, policy=None, instance=None, **kwargs):
        with allure.step(f"GET: {self.endpoint}{path}"):
            response = super().get_request(path=path)
            with allure.step(f"Response: {response}"):
                return response

    def post_request(self, path, data=None, policy=None, instance=None, **kwargs):
        with allure.step(f"POST: {self.endpoint}{path} | Data: {data}"):
            response = super().post_request(path=path, data=data)
            with allure.step(f"Response: {response}"):
                return response
