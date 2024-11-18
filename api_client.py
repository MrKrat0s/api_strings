import json

from requests import Session


def create_http_session():
    s = Session()
    s.verify = False
    s.trust_env = False
    return s


class RequesterAPI:
    def __init__(self):
        self.session = create_http_session()
        self.path = f"http://0.0.0.0:1234/api/"

    def json_from_request(self, path, request_method, data=""):
        response = self.session.request(
            request_method,
            url=f"{self.path}{path}",
            json=data,
        )
        return json.loads(response.text)

    def get_request(self, path):
        return self.json_from_request(path, "get")

    def post_request(self, path, data=None):
        return self.json_from_request(path, "post", data=data)

