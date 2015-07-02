from os import listdir, makedirs
from os.path import isdir, join
from re import compile
from shutil import move

from PlexOps import getcurrenttime


def uploadfiles(plexops_app):
    uploader_regex = {"name": compile(plexops_app.get_settings('plexname_regex')),
                      "season": compile(plexops_app.get_settings('plexseason_regex')),
                      "episode": compile(plexops_app.get_settings('plexep_regex'))}

    if not isdir(plexops_app.get_settings('server_location')):
        plexops_app.logger.critical("[%s] Critical Error: Server unreachable." % getcurrenttime())
        plexops_app.abort()

    for files in listdir(plexops_app.get_settings('operation_location')):
        if files.endswith(".mkv") and files[0] != "[":
            fdata = {'file': files, 'series': uploader_regex['name'].match(files).group(1),
                     'season': uploader_regex['season'].match(files).group(1),
                     'episode': uploader_regex['episode'].match(files).group(1)}
            fdata['season'] = str(int(fdata['season']))
            if not isdir(join(plexops_app.server_location, fdata['series'], "Season " + fdata['season'])):
                makedirs(join(plexops_app.server_location, fdata['series'], "Season " + fdata['season']))
                plexops_app.logger.info("[%s] Created directory for %s Season %s" % (
                    getcurrenttime(), fdata['series'], fdata['season']))

            move(join(plexops_app.operation_location, fdata['file']),
                 join(plexops_app.server_location, fdata['series'], "Season " + fdata['season'], fdata['file']))
            plexops_app.logger.info("[%s] Moved %s s%se%sto the server." % (
                getcurrenttime(), fdata['series'], fdata['season'], fdata['episode']))
