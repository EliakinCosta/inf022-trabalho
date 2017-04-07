import requests
from dateutil import parser as date_parser
import datetime
import pytz


class RepositoryFacade(object):

    def __init__(self, user_owner, repository):
        self.user_owner = user_owner
        self.repository = repository
        self.commits = []
        self.contributors = []

        self._load_commits()
        self._load_contributors()

    def _load_commits(self):
        has_next = True
        url = 'https://api.github.com/repositories/43975673/commits?page=62'
        headers = {'Authorization': 'token {0}'.format('45803467536d94d0dce8460755c2b4f3538fd7e7')}
        result = requests.get(url, headers=headers)
        print(result)
        if result.status_code!=200:
            return
        count = 0
        while has_next:
            print(result)
            commits = result.json()
            self.commits.extend([commit for commit in commits])
            link = result.headers
            count += 1
            print(count)
            link = link['Link']
            print(link)
            link = link.replace('<', '').replace('>', '')

            if not 'rel="next"' in str(link):
                has_next = False

            if has_next:
                next_link = link.split(',')[0]
                next_link = next_link.split(';')[0]
                url = next_link
                result = requests.get(url)

    def _load_contributors(self):
        contributors = []

        for commit in self.commits:
            if not commit['commit']['author']['email'] in [user['email'] for user in contributors]:
                contributors.append(dict(email=commit['commit']['author']['email'], name=commit['commit']['author']['name']))

        self.contributors.extend(contributors)

    def commits_by_window(self, start_period, end_pediod):
        return [commit for commit in self.commits if (date_parser.parse(commit['commit']['committer']['date'])>=start_period and
                                                      date_parser.parse(commit['commit']['committer']['date'])<=end_pediod)]

if __name__=='__main__':
    git_wrapper = RepositoryFacade('sandroandrade', 'emile-server')
    commits = git_wrapper.commits_by_window(datetime.datetime(2016, 9, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(2017, 10, 1, tzinfo=pytz.timezone('America/Bahia')))
    teste = None
    try:
        for commit in commits:
            teste = commit
            print(commit['commit']['author']['email'])
    except:
        print(teste)
