from api_client import RequesterAPI


class StringRequester(RequesterAPI):
    def get_strings(self):
        return self.get_request("string")

    def get_string(self, id):
        return self.get_request(f"string/{id}")

    def post_strings(self, data):
        return self.post_request("string", data=data)
