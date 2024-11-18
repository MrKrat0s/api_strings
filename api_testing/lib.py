from uuid import UUID

class Tools:
    @staticmethod
    def make_json(**kwargs):
        return {
            key if not key.startswith("_") else key[1:]: v for key, v in kwargs.items()
        }

    @staticmethod
    def is_palindrome(x):
        return str(x) == str(x)[::-1]

    @staticmethod
    def is_valid_uuid(uuid_to_test, version=4):
        try:
            uuid_obj = UUID(uuid_to_test, version=version)
        except ValueError:
            return False
        return str(uuid_obj) == uuid_to_test
