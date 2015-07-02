from os import listdir
from os.path import join
from re import compile
from shutil import move

from PlexOps import getcurrenttime, padandstringify


def rename(plexops_app):
    rename_regex = {'name': compile(plexops_app.get_settings('name_regex')),
                    'episode': compile(plexops_app.get_settings('episode_regex'))}

    for files in listdir(plexops_app.operation_location):
        if files.endswith(".mkv") and files[0] == "[":
            fdata = {"location": files, "name": rename_regex['name'].match(files).group(1),
                     "ep": padandstringify(rename_regex['episode'].match(files).group(1)), "season": "01"}
            fdata['name'] = fdata['name'].replace("_", " ")
            if fdata['name'] in plexops_app.get_settings('show_settings'):
                plexops_app.logger.info("[%s] Series %s has settings configured. Adjusting data..." % (
                    getcurrenttime(), fdata['name']))
                _showsettings = plexops_app.get_showsettings(fdata['name'])
                if 'season' in _showsettings:
                    fdata['season'] = padandstringify(_showsettings['season'])
                if 'adjust' in _showsettings:
                    fdata['ep'] = padandstringify(int(fdata['ep']) - _showsettings['adjust'])
                if 'altname' in _showsettings:
                    fdata['name'] = _showsettings['altname']

            move(join(plexops_app.operation_location, fdata['location']), join(plexops_app.operation_location,
                                                                               "%s - s%sse%s.mkv" % (
                                                                                   fdata['name'], fdata['season'],
                                                                                   fdata['ep'])))
