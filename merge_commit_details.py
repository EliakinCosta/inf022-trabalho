import json
import os


global_commits = []
global_commits_details = []


def get_commit_details(sha):
    try:
        local_details = [details['sha'] for details in global_commits_details]
        index = local_details.index(sha)
        return global_commits_details[index]
    except ValueError:
        return {}


def load_commits():
    files = os.listdir('./files')
    files.sort()
    for _file in files:
        if _file.split('.')[1]=='json':
            with open('./files/{0}'.format(_file), 'r') as evowave_file:
                commits = json.loads(evowave_file.read())
                for commit in commits:
                    commit.update(get_commit_details(commit['sha']))
                global_commits.extend(commits)
                print('novo arquivo carregado')


def load_commits_details():
    files = os.listdir('./details')
    files.sort()
    for _file in files:
        if _file.split('.')[1]=='json':
            with open('./details/{0}'.format(_file), 'r') as details_file:
                commits_details = json.loads(details_file.read())
                global_commits_details.extend([commit_details for commit_details in commits_details])


if __name__=='__main__':
    load_commits_details()
    load_commits()

    with open('new_data.json', 'w') as evowave_file:
        json.dump(global_commits, evowave_file)
