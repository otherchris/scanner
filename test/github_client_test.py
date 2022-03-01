from scanner.github_client import create_pull


def test_create_pull_from_gh_response():
    gh = GithubClient()
    gh.list_prs()
