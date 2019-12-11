import os
from pprint import pprint

import requests
from requests.auth import HTTPBasicAuth

base_url = os.environ["ZENDESK_URL"]
username = os.environ["SYS_ADMIN_USERNAME"]
key = os.environ["SYS_ADMIN_KEY"]


def get_zendesk(url_extension):
    response = requests.get(url=f"{base_url}{url_extension}",
                     auth=HTTPBasicAuth(username, key),
                     headers={'Accept': 'application/json'})

    return response


def get_users():
    url_extension = "users"
    pprint(get_zendesk(url_extension).json())


get_users()