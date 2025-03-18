import os

def rename_file(dir_path, name, from_num, digit):
    try:
        target_files = os.listdir(dir_path)
    except PermissionError:
        print(dir_path + 'が開けません')
        return
    if(len(target_files) == 0):
        print(dir_path + 'にファイルがありません')
        return
    num = from_num
    for f in target_files:
        old_name = os.path.join(dir_path, f)
        n = str(num).zfill(digit)
        ext = os.path.splitext(f)[1]
        new_name = os.path.join(dir_path, name + n + ext)
        os.rename(old_name, new_name)
        num += 1