import requests
from dateutil import parser as date_parser
import datetime
import pytz
import json
import time


class RepositoryFacade(object):

    def __init__(self, user_owner, repository):
        self.user_owner = user_owner
        self.repository = repository
        self.commits = []
        self.contributors = []

        self._load_commits()
        #self._load_contributors()

    def _load_commits(self):
        count = 0
        has_next = True
        url = 'https://api.github.com/repositories/43975673/commits?per_page=100&since=2012-04-09T00:00:01Z&until=2013-04-08T11:59:59Z'
        headers = {'Authorization': 'token {0}'.format('387292809a22b21fbb1661246aa1d340d8700e87')}
        result = requests.get(url, headers=headers)
        print(result)
        if result.status_code!=200:
            return
        while has_next:
            print(result)
            commits = result.json()
            self.commits.extend([commit for commit in commits])
            header = result.headers
            count += 1
            print(count)
            link = header.get('Link')
            print(link)

            if count%30==0:
                time.sleep(65)

            if not 'rel="next"' in str(link):
                has_next = False

            if has_next:
                link = link.replace('<', '').replace('>', '')
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
    #15 2012-2013 NAO foi executado ainda
    git_wrapper = RepositoryFacade('sandroandrade', 'emile-server')
    with open('data_15.json', 'w') as evowave_file:
        json.dump(git_wrapper.commits, evowave_file)
