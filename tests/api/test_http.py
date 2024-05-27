import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get("https://api.github.com/zen")
    print(r.text)


@pytest.mark.http
def test_second_request():
    r = requests.get("https://api.github.com/users/defunkt")
    body = r.json()
    headers = r.headers

    assert body["name"] == "Chris Wanstrath"
    assert r.status_code == 200
    assert headers["Server"] == "GitHub.com"
    # print(f"Pesponse Body is {r.json()}")
    # print(f"Pesponse Status is {r.status_code}")
    # print(f"Pesponse Headers are {r.headers}")


@pytest.mark.http
def test_status_code_request():
    r = requests.get("https://api.github.com/users/liudmyla_kaniuk")

    assert r.status_code == 404
