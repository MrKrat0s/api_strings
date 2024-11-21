from uuid import UUID
from requests import Session


def is_palindrome(x):
    return str(x) == str(x)[::-1]


def is_valid_uuid(uuid_to_test, version=4):
    if not isinstance(uuid_to_test, str):
        return False
    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test


def create_http_session():
    s = Session()
    s.verify = False
    s.trust_env = False
    return s



