from dateutil import parser as date_parser
import datetime
import pytz
import json
import time
import os
import list_windows
import requests


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
        with open('./new_data.json', 'r') as evowave_file:
            commits = json.loads(evowave_file.read())
            self.commits.extend([commit for commit in commits])

    def _load_contributors(self):
        contributors = []

        for commit in self.commits:
            if not commit['commit']['author']['email'] in [user['email'] for user in contributors]:
                contributors.append(dict(email=commit['commit']['author']['email'], name=commit['commit']['author']['name']))
                self.contributors_windows[str(commit['commit']['author']['email'])] = set([])

            current_window = self._commit_window(commit)
            if current_window:
                self.contributors_windows[commit['commit']['author']['email']].add(current_window)

        self.contributors.extend(contributors)

    def _commit_window(self, commit):
        for window in list_windows.list_windows():
            if((date_parser.parse(commit['commit']['committer']['date'])>=window[1]) and
                date_parser.parse(commit['commit']['committer']['date'])<=window[2]  and
                not (date_parser.parse(commit['commit']['committer']['date'])>=window[3] and
                    date_parser.parse(commit['commit']['committer']['date'])<=window[4])):
                return window[0]


    def commits_by_window(self, start_period, end_pediod, ignored_period_start, ignored_period_end, contributor):
        return [commit for commit in self.commits if (date_parser.parse(commit['commit']['committer']['date'])>=start_period and
                                                      date_parser.parse(commit['commit']['committer']['date'])<=end_pediod and
                                                      commit['commit']['author']['email']==contributor and
                                                      not (date_parser.parse(commit['commit']['committer']['date'])>=ignored_period_start and
                                                           date_parser.parse(commit['commit']['committer']['date'])<=ignored_period_end))]


if __name__=='__main__':
    git_wrapper = RepositoryFacade('KDE', 'krita')
    _commits = []
    _contributors = []
    print(len(git_wrapper.commits))
    count = 0

    for contributor in git_wrapper.contributors:
        commits = git_wrapper.commits_by_window(datetime.datetime(2009, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                                      datetime.datetime(2010, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                                      datetime.datetime(1980, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1981, 9, 7, tzinfo=pytz.timezone('America/Bahia')), contributor['email'])
        count += len(commits)

    print(count)
