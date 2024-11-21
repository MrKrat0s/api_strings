import json

from lib.tools import create_http_session


class RequesterAPI:
    def __init__(self, hostname):
        self.session = create_http_session()
        self.path = f"http://{hostname}/api/"

    def make_request(self, path, request_method, data=None):
        try:
            result_path = f"{self.path}{path}"
            return self.session.request(
                request_method,
                url=result_path,
                json=data,
            )
        except ConnectionError:
            raise Exception('Ошибка соединения')

    def json_from_request(self, path, request_method, data=""):
        response = self.make_request(
                path,
                request_method,
                data=data,
            )
        return response

    def get_request(self, path):
        return self.json_from_request(path, "get")

    def post_request(self, path, data=None):
        return self.json_from_request(path, "post", data=data)
