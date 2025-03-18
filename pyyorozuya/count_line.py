from pyyorozuya.get_files import get_files as gf

def count_line(path, trim_blank = False):
    line_counter = 0
    target_files = gf(path)
    for file in target_files:
        try:
            with open(file, encoding = 'UTF-8') as f:
                for l in f:
                    if trim_blank and l.isspace():
                        continue
                    line_counter += 1
        except Exception:
            print(file + 'でエラー')
    return line_counter