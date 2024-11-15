import os

from pydriller import git


def clone_repositories(file_path):
    with open(file_path, 'r') as file:
        repos = file.readlines()

    for repo in repos:
        try:
            repo_url = repo.strip()
            repo_name = repo_url.split('/')[-1].replace('.git', '')
            if not os.path.exists(repo_name):
                git.Repo.clone_from(repo_url, repo_name)
            print(f"Cloned {repo_name}")
        except Exception as ex:
            print(f"cloning {repo} failed because of {ex}")