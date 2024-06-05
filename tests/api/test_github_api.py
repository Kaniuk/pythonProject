import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("someinteresteduserfromgithub")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    assert r["total_count"] == 57
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("someinteresteduserfromgithub")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0


@pytest.mark.api
def test_repo_commits_exist(github_api):
    owner = "octocat"
    repo = "Hello-World"
    r = github_api.search_commits(owner, repo)
    assert isinstance(r, list)
    assert len(r) > 0


@pytest.mark.api
def test_repo_commits_statuses(github_api):
    owner = "octocat"
    repo = "Hello-World"
    branch = "master"
    r = github_api.search_commit_statuses(owner, repo, branch)
    print(r["state"])
    assert r["state"] != "failure"


@pytest.mark.api
def test_get_watchers(github_api):
    owner = "octocat"
    repo = "Hello-World"
    r = github_api.get_watchers(owner, repo)
    assert len(r) > 1
