import os

from zen_tool_box import zen_tools

base_url = os.environ["ZENDESK_URL"]


def test_get_zendesk():
    url = f"{base_url}users.json"
    response = zen_tools.get_zendesk(url)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_get_all_users():
    all_users = zen_tools.get_all_users()
    assert isinstance(all_users, list)
    for user in all_users:
        assert isinstance(user, dict)
