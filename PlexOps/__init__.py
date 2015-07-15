from json import load
from sys import exit
from time import strftime


class PlexOps:
    def __init__(self):
        try:
            self.settings = load(open("settings.json"))
        except FileNotFoundError:
            print("[%s] Critical Error: Settings.json not found." % getcurrenttime())
            self.abort()
        self.operation_location = self.settings['operation_location']
        self.server_location = self.settings['server_location']

    def abort(self):
        print("Terminating PlexOps...")
        exit()

    def get_settings(self, setting):
        return self.settings[setting]

    def get_showsettings(self, show):
        return self.settings['show_settings'][show]


class Video:
    def __init__(self, original_location, name, episode):
        self.original_location = original_location
        self.name = name
        self.episode = episode


def padandstringify(number):
    return str(number) if number >= 10 else "0" + str(number)

def getcurrenttime():
    return strftime("%m-%d-%Y %H:%M")