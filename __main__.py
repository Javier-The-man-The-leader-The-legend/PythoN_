from typing import Callable
from os import listdir, rename

def rename_files(pth: str, filter_func: Callable[str, bool], rename_func: Callable[str, str]) -> bool: 
    files = listdir(path)
    # files_wanted = []
    # for filename in files:
    #     if filter_func(filename):
    #         files_wanted.append(filename)
    # files_wanted = [filename for filename in files if filter_func(filename)]
    files_wanted = filter(filter_func, files)
    # for filename in files_wanted:
    #     new_filename = rename_func(filename)
    #     rename(path + "/" + filename, path + "/" + new_filename)
    # def renamer(path, old):
    #     new = rename_func(old)
    #     rename(path + "/" + old, path + "/" + new)
    # map(renamer, files_wanted)
    map(lambda path, old: rename(path + "/" + old, path + "/" + rename_func(old)), files_wanted)
# def mp3_filter(filename: str) -> bool:
#     return filename.endswith(".mp3")
def filter_creator(type: str, options: str) -> Callable[str, bool]:
    if type == "extension":
        def filter_func(name: str):
            exstension = name.rpartition(".")[0]
            return exstension == options
        return filter_func
    elif type == "search":
        def filter_func(name: str) -> bool:
            filename = name.rpartition(".")[2]
            return filename.find(option) > -1
        return filter_func