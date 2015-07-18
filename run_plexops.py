from PlexOps import getcurrenttime, PlexOps
from PlexOps.renamer import rename
from PlexOps.uploader import uploadfiles

if __name__ == "__main__":
    p = PlexOps()
    print("[%s] Starting renamer..." % getcurrenttime())
    rename(p)
    print("[%s] Renaming complete. \n[%s] Starting uploader..." % (getcurrenttime(), getcurrenttime()))
    uploadfiles(p)
    print("[%s] Uploading complete. Aborting PlexOps..." % getcurrenttime())
    p.abort()