from dateutil import parser as date_parser
import datetime
import pytz
import json
import time
import os
import list_windows


class RepositoryFacade(object):

    def __init__(self, user_owner, repository):
        self.user_owner = user_owner
        self.repository = repository
        self.commits = []
        self.contributors = []
        self.contributors_windows = {}

        self._load_commits()
        self._load_contributors()

    def _load_commits(self):
        files = os.listdir('./files')
        files.sort()
        for _file in files:
            if _file.split('.')[1]=='json':
                with open('./files/{0}'.format(_file), 'r') as evowave_file:
                    commits = json.loads(evowave_file.read())
                    self.commits.extend([commit for commit in commits])

    def _load_contributors(self):
        contributors = []

        for commit in self.commits:
            if not commit['commit']['author']['email'] in [user['email'] for user in contributors]:
                contributors.append(dict(email=commit['commit']['author']['email'], name=commit['commit']['author']['name']))
                self.contributors_windows[str(commit['commit']['author']['email'])] = set([])
            self.contributors_windows[commit['commit']['author']['email']].add(self._commit_window(commit))

        self.contributors.extend(contributors)

    def _commit_window(self, commit):
        for window in list_windows.list_windows():
            if(date_parser.parse(commit['commit']['committer']['date'])>=window[1] and
               date_parser.parse(commit['commit']['committer']['date'])<=window[2]):
               return window[0]


    def commits_by_window(self, start_period, end_pediod, contributor):
        return [commit for commit in self.commits if (date_parser.parse(commit['commit']['committer']['date'])>=start_period and
                                                      date_parser.parse(commit['commit']['committer']['date'])<=end_pediod and
                                                      commit['commit']['author']['email']==contributor)]

if __name__=='__main__':
    #18 2016-2017 NAO foi executado ainda
    git_wrapper = RepositoryFacade('sandroandrade', 'emile-server')
    print(git_wrapper.contributors_windows)
    print(len(git_wrapper.contributors_windows))
