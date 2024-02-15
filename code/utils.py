from settings import *
from os import walk
from os.path import join


def get_bg_paths(path):
    bg_list = []
    dir_path = join(*path)
    for root, dirs, files in walk(dir_path):
        for f in files:
            bg_list.append(join(dir_path, f))

    return bg_list
