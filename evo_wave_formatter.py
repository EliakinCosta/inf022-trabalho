import repository_facade
from dateutil import parser as date_parser
import datetime
import pytz
import json


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



def list_windows():
    windows = []

    windows.append((1, datetime.datetime(2016, 5, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(2016, 6, 1, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((2, datetime.datetime(2016, 6, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(2016, 7, 1, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((3, datetime.datetime(2016, 7, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(2016, 8, 1, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((4, datetime.datetime(2016, 8, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(2016, 9, 1, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((5, datetime.datetime(2016, 9, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(2016, 10, 1, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((6, datetime.datetime(2016, 10, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(2016, 11, 1, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((7, datetime.datetime(2016, 11, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(2016, 12, 1, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((8, datetime.datetime(2016, 12, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(2017, 1, 1, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((9, datetime.datetime(2017, 1, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(2017, 2, 1, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((10, datetime.datetime(2017, 2, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(2017, 3, 1, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((11, datetime.datetime(2017, 3, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(2017, 4, 1, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((12, datetime.datetime(2017, 4, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime.now(tz=pytz.timezone('America/Bahia'))))

    return windows


def load_windows_to_sectors(sectors, general_windows):
    for sector in sectors:
        for window in general_windows:
            commits_by_window = git_wrapper.commits_by_window(window[1], window[2])
            if [commit for commit in commits_by_window if commit['commit']['author']['email'] == sector.sector_name]:
                sector.add_window(Window(window[0], window[1], window[2], sector.sector_name))


def load_molecules_to_sectors(sectors):
    count = 0
    for sector in sectors:
        for window in sector.windows:
            commits_by_window = git_wrapper.commits_by_window(window.starts, window.ends)
            commits_by_sector = [commit['commit']['message'] for commit in commits_by_window if commit['commit']['author']['email'] == window.sector_parent]
            for commit in commits_by_sector:
                window.add_molecule(Molecule(dict(message=commit), window.position))


if __name__=='__main__':
    commits = git_wrapper.commits

    sectors = []
    general_windows = list_windows()

    for user in git_wrapper.contributors:
        sectors.append(Sector(user['email'], 0.066))

    load_windows_to_sectors(sectors, general_windows)
    load_molecules_to_sectors(sectors)

    json_dict = dict(period={"starts": "01/09/1978 00:00:00 +0000", "ends": "07/09/2017 00:00:00 +0000"},
                     query="",
                     window={
                         "size": 25,
                         "amount": 12,
                         "mode": "GLOBAL"
                     },
                     sector={"label": "krita"},
                     sectors=[sector.as_dict() for sector in sectors])


    with open('data.json', 'w') as evowave_file:
        json.dump(json_dict, evowave_file)
