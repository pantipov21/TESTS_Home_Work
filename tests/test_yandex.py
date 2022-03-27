import pytest
from yandex import create_folder_YA_REST_API

FOLDER_NAME = '!_test_folder'

fixture = [
    (FOLDER_NAME, 201, "OK"),
    (FOLDER_NAME, 400, "Incorrect data"),
    (FOLDER_NAME, 401, "Non-authorized request"),
    (FOLDER_NAME, 403, "API is unreachable"),
    (FOLDER_NAME, 404, "Resource not found"),
    (FOLDER_NAME, 406, "Resource format is not acceptable"),
    (FOLDER_NAME, 409, "The folder already exists"),
    (FOLDER_NAME, 423, "Resource has blocked"),
    (FOLDER_NAME, 429, "Too many requests"),
    (FOLDER_NAME, 503, "Service is temporary unreachable"),
    (FOLDER_NAME, 507, "Not enough disk space")
]


class TestFunctionsPytest:
    def setup(self):
        print('===> setup')

    def teardown(self):
        print('===> teardown')

    @pytest.mark.parametrize("folder_name, status_code, descr", fixture)
    def test_create_folder_yandex_api(self, folder_name, status_code, descr):
        assert create_folder_YA_REST_API(folder_name) == status_code


