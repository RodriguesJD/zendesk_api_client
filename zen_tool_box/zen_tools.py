import os
from pprint import pprint
from typing import Union
import requests
from requests.auth import HTTPBasicAuth

base_url = os.environ["ZENDESK_URL"]
username = os.environ["SYS_ADMIN_USERNAME"]
key = os.environ["SYS_ADMIN_KEY"]


def get_zendesk(url) -> object:
    """
    This function handles auth and service for Zendesk restAPI access.

    Returns: service: Rest API response object
    """
    response = requests.get(url=f"{url}",
                            auth=HTTPBasicAuth(username, key),
                            headers={'Accept': 'application/json'})

    return response


def get_all_users() -> list:
    """
    Get all data on all users and return it as a list of dictionaries.

    :return all_user_data: List of dictionaries of all users data.
    """
    all_user_data = []
    url_extension = "users.json"
    url = f"{base_url}{url_extension}"
    while url:
        response = get_zendesk(url).json()
        next_page = response['next_page']
        users = response['users']
        url = next_page
        for user in users:
            all_user_data.append(user)

    return all_user_data


def find_user(user_email: str) -> Union[dict, bool]:
    """
    Search for user by email.

    :param user_email: Users email address.
    :return user_data: Users data in a dictionary.
    """
    found_user = False
    url_extension = f"search.json?query={user_email}"
    url = f"{base_url}{url_extension}"
    if user_email:
        response = get_zendesk(url).json()
        if response['count'] != 0:
            for result in response['results']:
                if result['result_type'] == 'user' and user_email == result['email']:
                    found_user = result
    else:
        pass

    return found_user



print(find_user("jeremy.rodrigues@ext.li.me"))