import sys
sys.path.append("/usr/lib/python3/dist-packages")
import requests

TOKEN = ''


def create_folder_YA_REST_API(folder_name):
    url = "https://cloud-api.yandex.net:443/v1/disk/resources/"
    params = {"path": folder_name}
    headers = {"Authorization": f'OAuth {TOKEN}'}

    print('Upload link request is sending...')
    resp = requests.put(url, params=params, headers=headers)
    return resp.status_code

