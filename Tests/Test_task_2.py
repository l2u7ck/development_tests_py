import pytest
import requests
from dotenv import load_dotenv
from dotenv import dotenv_values
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    print(load_dotenv(dotenv_path))


class TestYandexDick:
    def setup_method(self):
        self.headers = {
            'Authorization': f'OAuth {dotenv_values()['TOKEN_YANDEX_DICK']}'
        }
        self.params = {
            "path": 'New_Folder'
        }
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def teardown_class(self):
        TestYandexDick.setup_method(self)
        requests.delete(self.url, params=self.params, headers=self.headers)

    @pytest.mark.parametrize(
        "key, value, status", (
            ['path', "New_Folder", 201],
            ['path', "New_Folder", 409],
            ['pat', "New_Folder", 400],
        )
    )
    def test_create_folder(self, key, value, status):
        self.status = status
        self.params = {
            key: value
        }
        response = requests.put(self.url, params=self.params, headers=self.headers)
        assert response.status_code == self.status

    @pytest.mark.parametrize(
        "auth, token, status", (
                ['Authorization', f'{dotenv_values()['TOKEN_YANDEX_DICK']}', 200],
                ['Authorization', 'y0_AgAAAABAqmI4AADGJKDJK', 401],
                ['Auth', f"{dotenv_values()['TOKEN_YANDEX_DICK']}", 401],
        )
    )
    @pytest.mark.xfail
    def test_authorization(self, auth, token, status):
        self.status = status
        self.headers = {
            auth: token
        }
        response = requests.get(self.url, params=self.params, headers=self.headers)
        assert response.status_code == self.status


