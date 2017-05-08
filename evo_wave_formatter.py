import repository_facade
from dateutil import parser as date_parser
import datetime
import pytz
import json
import list_windows


git_wrapper = repository_facade.RepositoryFacade('KDE', 'krita')


class Sector(object):

    def __init__(self, sector_name, angle):
        self.sector_name = sector_name
        self.angle = angle
        self.windows = []

    def add_window(self, window):
        self.windows.append(window)

    def as_dict(self):
        sector_name = [user['name'] for user in git_wrapper.contributors if self.sector_name==user['email']][0]
        return dict(angle=self.angle, label=sector_name, windows=[window.as_dict() for window in self.windows])


class Window(object):

    def __init__(self, position , starts, ends, ignored_start, ignored_end, sector_parent):
        self.position = position
        self.starts = starts
        self.ends = ends
        self.ignored_start = ignored_start
        self.ignored_end = ignored_end
        self.sector_parent = sector_parent
        self.molecules = []

    def add_molecule(self, molecule):
        self.molecules.append(molecule)

    def as_dict(self):
        return dict(position=self.position, molecules=[molecule.as_dict() for molecule in self.molecules])


class Molecule(object):
    """ It represents molecule structure including your window position. """

    def __init__(self, data, window_position):
        self.data = data
        self.window_position = window_position
        self.define_color()

    def define_color(self):
        if self.data['lines_modified'] <= 20 or  self.data['files_modified'] <= 2:
            self.color = 'FF66FFFF'
        elif self.data['lines_modified'] <= 40 or  self.data['files_modified'] <= 4:
            self.color = 'FF5079ff'
        elif self.data['lines_modified'] <= 60 or  self.data['files_modified'] <= 6:
            self.color = 'FFFFE800'
        elif self.data['lines_modified'] <= 80 or  self.data['files_modified'] <= 8:
            self.color = 'FFF67B5E'
        elif self.data['lines_modified'] >= 80 or  self.data['files_modified'] >= 8:
            self.color = 'FF85090B'

    def as_dict(self):
        return dict(color=self.color, data=self.data)


def load_windows_to_sectors(sectors, general_windows):
    for sector in sectors:
        for window_position in git_wrapper.contributors_windows[sector.sector_name]:
            sector.add_window(Window(general_windows[window_position-1][0],
                                     general_windows[window_position-1][1],
                                     general_windows[window_position-1][2],
                                     general_windows[window_position-1][3],
                                     general_windows[window_position-1][4],
                                     sector.sector_name))


def load_molecules_to_sectors(sectors):
    count = 1
    for sector in sectors:
        for window in sector.windows:
            print(window.starts, window.ends)
            print(len(git_wrapper.commits_by_window(window.starts, window.ends, window.ignored_start, window.ignored_end, window.sector_parent)))
            commits_by_sector = [dict(files_modified=len(commit.get('files', [])), lines_modified=commit['stats']['total']) for commit in git_wrapper.commits_by_window(window.starts, window.ends, window.ignored_start, window.ignored_end, window.sector_parent) if commit.get('stats')]
            for commit in commits_by_sector:
                window.add_molecule(Molecule(commit, window.position))
                print('commit', count)
                count += 1


if __name__=='__main__':
    commits = git_wrapper.commits
    print(len(commits))
    sectors = []
    general_windows = list_windows.list_windows()

    for user in git_wrapper.contributors:
        sectors.append(Sector(user['email'], round((100/len(general_windows)) * 0.01, 4)))

    load_windows_to_sectors(sectors, general_windows)
    load_molecules_to_sectors(sectors)

    json_dict = dict(period={"starts": "01/09/1978 00:00:00 +0000", "ends": "07/09/2017 00:00:00 +0000"},
                     query="",
                     window={
                         "size": 10,
                         "amount": len(general_windows),
                         "mode": "GLOBAL"
                     },
                     sector={"label": "krita"},
                     sectors=[sector.as_dict() for sector in sectors])


    with open('data.json', 'w') as evowave_file:
        json.dump(json_dict, evowave_file)
