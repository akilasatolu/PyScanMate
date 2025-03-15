import os
import re
from pyscanmate.format_txt import format_txt as ft

def get_files(path, reg = r'.*$', hidden = False):
    files = []
    reg_ptn = re.compile(reg)
    def find_file(path):
        try:
            items = os.listdir(path)
        except PermissionError:
            print(path + 'が開けません')
            return
        if(len(items) == 0):
            return
        for item in items:
            if not hidden and item.startswith('.'):
                continue
            full_path = os.path.join(path, item)
            if os.path.isfile(full_path):
                if reg_ptn.search(item):
                    ft(full_path, r'\\', '/')
                    files.append(full_path)
                continue
            find_file(full_path)
    find_file(path)
    return files