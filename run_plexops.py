from PlexOps import getcurrenttime, PlexOps
from PlexOps.renamer import rename
from PlexOps.uploader import uploadfiles

if __name__ == "__main__":
    p = PlexOps()
    p.logger.info("[%s] PlexOps initialized." % getcurrenttime())
    p.logger.info("[%s] Running renamer..." % getcurrenttime())
    rename(p)
    p.logger.info("[%s] Renaming complete!" % getcurrenttime())
    p.logger.info("[%s] Running uploader..." % getcurrenttime())
    uploadfiles(p)
    p.logger.info("[%s] Uploading complete!" % getcurrenttime())
    p.abort()