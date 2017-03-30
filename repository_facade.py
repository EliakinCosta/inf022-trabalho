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
        url = 'https://api.github.com/repos/{0}/{1}/commits'.format(self.user_owner, self.repository)
        result = requests.get(url)
        if result.status_code!=200:
            return

        commits = result.json()
        self.commits.extend([commit for commit in commits])

    def _load_contributors(self):
        url = 'https://api.github.com/repos/{0}/{1}/contributors'.format(self.user_owner, self.repository)
        result = requests.get(url)
        if result.status_code!=200:
            return

        contributors = result.json()
        self.contributors.extend([user['login'] for user in contributors])

    def commits_by_window(self, start_period, end_pediod):
        return [commit for commit in self.commits if date_parser.parse(commit['commit']['author']['date'])>start_period and
                                              date_parser.parse(commit['commit']['author']['date'])<=end_pediod]


if __name__=='__main__':
    git_wrapper = RepositoryFacade('sandroandrade', 'emile-server')
    print(len(git_wrapper.commits_by_window(datetime.datetime(2017, 1, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime.now(tz=pytz.timezone('America/Bahia')))))
