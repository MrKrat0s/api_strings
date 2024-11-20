class MakeJson:
    @staticmethod
    def make_json(**kwargs):
        return {
            key if not key.startswith("_") else key[1:]: v for key, v in kwargs.items()
        }