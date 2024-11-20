import json
from jsonschema import validate


class JsonTools:
    @staticmethod
    def make_json(**kwargs):
        return {
            key if not key.startswith("_") else key[1:]: v for key, v in kwargs.items()
        }

    @staticmethod
    def prepare_answer(response):
        return response.status_code, json.loads(response.text)

    @staticmethod
    def check_json_scheme(response_json, required_json):
        try:
            validate(instance=response_json, schema=required_json)
            return True
        except json.decoder.JSONDecodeError:
            return False
