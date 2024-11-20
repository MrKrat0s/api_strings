import pytest


def pytest_addoption(parser):
    parser.addoption("--host", required=True,  help='Адрес сервера')
    parser.addoption("--port", required=True, help='Порт сервера')


@pytest.fixture(scope='session')
def hostname(pytestconfig):
    return f"{pytestconfig.getoption("--host")}:{pytestconfig.getoption("--port")}"
