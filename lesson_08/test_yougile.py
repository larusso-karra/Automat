import requests
from YouGileAPI import YouGileApi

api = YouGileApi("https://ru.yougile.com")

# логин и пароль
login = "kosmik13@mail.ru"
password = "skypass"
company_name = "Constantine"
company_id = api.get_company_id(login, password, company_name)
keys_list = api.get_auth_keys(login, password, company_id)
auth_key = keys_list[0]["key"]


def test_get_project_list_pozitive():
    get_project_list = api.get_project_list(auth_key)
    assert get_project_list.status_code == 200


def test_get_project_list_negative():
    get_project = api.get_project_list("")
    assert get_project.status_code == 401


def test_project_list_pozitive():
    project_list = api.get_project_list(auth_key).json()
    assert len(project_list) > 0


def test_create_project_pozitive():
    project_list_before_create = api.get_project_list(auth_key).json().get("content")
    api.create_project("ПРивет!", auth_key)
    project_list_after_create = api.get_project_list(auth_key).json().get("content")
    assert len(project_list_after_create) > len(project_list_before_create)


def test_create_project_negative():
    project_list_before_create = api.get_project_list(auth_key).json().get("content")
    api.create_project(None, auth_key)
    project_list_after_create = api.get_project_list(auth_key).json().get("content")
    assert len(project_list_after_create) == len(project_list_before_create)


def test_get_project_info_pozitive():
    project_list = api.get_project_list(auth_key).json().get("content")
    project_id = project_list[0]["id"]
    project_info = api.get_project_info(project_id, auth_key)
    assert project_info["id"] == project_id


def test_get_project_info_negative():
    project_inf = api.get_project_info("1", auth_key)
    assert project_inf['statusCode'] == 404


def test_change_project_pozitive():
    api.create_project("Проект для изменения", auth_key)
    project_list_before = api.get_project_list(auth_key).json().get("content")
    project_id = project_list_before[0]["id"]
    project_title_before = api.get_project_info(project_id, auth_key).get("title")
    api.change_project(project_id, auth_key, False, "Измененный проект")
    project_title_after = api.get_project_info(project_id, auth_key).get("content")
    assert project_title_before != project_title_after


def test_change_project_negative():
    change_project = api.change_project("1", auth_key, True, None)
    assert change_project['statusCode'] == 404