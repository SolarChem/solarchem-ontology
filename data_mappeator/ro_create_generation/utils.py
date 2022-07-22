import shutil
import os

def clean_directory(dir):
    # Deleting an non-empty folder
    dir_path = rf"{dir}"
    shutil.rmtree(dir_path, ignore_errors=True)

    os.mkdir(dir)