from PlexOps import PlexOps
from PlexOps.renamer import rename
from PlexOps.uploader import uploadfiles

if __name__ == "__main__":
    p = PlexOps()
    print("Starting renamer...")
    rename(p)
    print("Renaming complete. \n Starting uploader...")
    uploadfiles(p)
    print("Uploading complete. Aborting PlexOps...")
    p.abort()