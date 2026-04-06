import requests

base_url = "https://ru.yougile.com"
api_key = "YxA5mvVIe6JBiJMdSC080udQx+K8FZo2PGqqaAnoSvZbdjjNhFZcq8wFSR4jFq3i"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

TIMEOUT = 10


def test_add_new_project_positive():
    """Позитивное тестирование: добавление нового проекта"""
    title = "MAX"
    payload = {"title": title}

    resp = requests.post(
        url=f"{base_url}/api-v2/projects",
        headers=HEADERS,
        json=payload,
        timeout=TIMEOUT
    )
    assert resp.status_code == 201


def test_add_new_project_negative():
    """Негативное тестирование: добавление проекта с пустым title"""
    payload = {"title": ""}

    resp = requests.post(
        url=f"{base_url}/api-v2/projects",
        headers=HEADERS,
        json=payload,
        timeout=TIMEOUT
    )
    assert resp.status_code == 400


def test_change_project_positive():
    """Позитивное тестирование: изменение проекта"""
    # Создать новый проект
    title = "VK"
    payload = {"title": title}
    resp = requests.post(
        url=f"{base_url}/api-v2/projects",
        headers=HEADERS,
        json=payload,
        timeout=TIMEOUT
    )
    assert resp.status_code == 201

    resp_body = resp.json()
    project_id = resp_body["id"]

    # Изменить название проекта
    new_title = "ГосУслуги"
    new_payload = {"title": new_title}
    resp = requests.put(
        url=f"{base_url}/api-v2/projects/{project_id}",
        headers=HEADERS,
        json=new_payload,
        timeout=TIMEOUT
    )
    assert resp.status_code == 200

    # Получить изменённый проект и проверить название
    resp = requests.get(
        url=f"{base_url}/api-v2/projects/{project_id}",
        headers=HEADERS,
        timeout=TIMEOUT
    )
    assert resp.status_code == 200
    resp_body = resp.json()
    actual_title = resp_body["title"]
    assert actual_title == new_title


def test_change_project_negative():
    """Негативное тестирование: попытка установить пустой title"""
    # Создать проект
    title = "VK"
    payload = {"title": title}
    resp = requests.post(
        url=f"{base_url}/api-v2/projects",
        headers=HEADERS,
        json=payload,
        timeout=TIMEOUT
    )
    assert resp.status_code == 201

    resp_body = resp.json()
    project_id = resp_body["id"]

    # Изменить title на пустую строку
    new_payload = {"title": ""}
    resp = requests.put(
        url=f"{base_url}/api-v2/projects/{project_id}",
        headers=HEADERS,
        json=new_payload,
        timeout=TIMEOUT
    )
    assert resp.status_code == 400

    # Проверить, что название не изменилось
    resp = requests.get(
        url=f"{base_url}/api-v2/projects/{project_id}",
        headers=HEADERS,
        timeout=TIMEOUT
    )
    assert resp.status_code == 200
    resp_body = resp.json()
    actual_title = resp_body["title"]
    assert actual_title == title  # осталось прежним


def test_get_project_ID_positive():
    """Позитивное тестирование: получение проекта по ID"""
    title = "VK"
    payload = {"title": title}
    resp = requests.post(
        url=f"{base_url}/api-v2/projects",
        headers=HEADERS,
        json=payload,
        timeout=TIMEOUT
    )
    assert resp.status_code == 201

    project_id = resp.json()["id"]

    resp = requests.get(
        url=f"{base_url}/api-v2/projects/{project_id}",
        headers=HEADERS,
        timeout=TIMEOUT
    )
    assert resp.status_code == 200
    assert resp.json()["title"] == title


def test_get_project_ID_negative():
    """Негативное тестирование: запрос несуществующего ID"""
    fake_id = "00000000-0000-0000-0000-000000000000"
    resp = requests.get(
        url=f"{base_url}/api-v2/projects/{fake_id}",
        headers=HEADERS,
        timeout=TIMEOUT
    )
    assert resp.status_code == 404
