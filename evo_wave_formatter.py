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

    def __init__(self, position , starts, ends, sector_parent):
        self.position = position
        self.starts = starts
        self.ends = ends
        self.sector_parent = sector_parent
        self.molecules = []

    def add_molecule(self, molecule):
        self.molecules.append(molecule)

    def as_dict(self):
        return dict(position=self.position, molecules=[molecule.as_dict() for molecule in self.molecules])


class Molecule(object):
    """ It represents molecule structure including your window position. """

    def __init__(self, data, window_position, color='FFFF0000'):
        self.data = data
        self.window_position = window_position
        self.color = color

    def as_dict(self):
        return dict(color=self.color, data=self.data)


def load_windows_to_sectors(sectors, general_windows):
    for sector in sectors:
        for window_position in git_wrapper.contributors_windows[sector.sector_name]:
            sector.add_window(Window(general_windows[window_position-1][0], general_windows[window_position-1][1], general_windows[window_position-1][2], sector.sector_name))
            print(sector.sector_name, general_windows[window_position-1])


def load_molecules_to_sectors(sectors):
    count = 0
    for sector in sectors:
        for window in sector.windows:
            commits_by_sector = [commit['commit']['message'] for commit in git_wrapper.commits_by_window(window.starts, window.ends, window.sector_parent)]
            for commit in commits_by_sector:
                window.add_molecule(Molecule(dict(message=commit), window.position))
                print('commit')


if __name__=='__main__':
    commits = git_wrapper.commits

    sectors = []
    general_windows = list_windows.list_windows()

    for user in git_wrapper.contributors:
        sectors.append(Sector(user['email'], 0.0025))

    load_windows_to_sectors(sectors, general_windows)
    load_molecules_to_sectors(sectors)

    json_dict = dict(period={"starts": "01/09/1978 00:00:00 +0000", "ends": "07/09/2017 00:00:00 +0000"},
                     query="",
                     window={
                         "size": 12,
                         "amount": 19,
                         "mode": "GLOBAL"
                     },
                     sector={"label": "krita"},
                     sectors=[sector.as_dict() for sector in sectors])


    with open('data.json', 'w') as evowave_file:
        json.dump(json_dict, evowave_file)
