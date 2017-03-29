import requests


def colaborators(user, repo):
    url = 'https://api.github.com/repos/{0}/{1}/collaborators'.format(user, repo)
    print(url)
    result = requests.get(url)
    print(result)
    if result.status_code!=200:
        return 'invalid repo or user'
    
    colaborators = result.json()
    return [user['login'] for user in colaborators]


def colaborators(use)


if __name__=='__main__':
    print(colaborators('EliakinCosta', 'editor-framework-inf011'))
