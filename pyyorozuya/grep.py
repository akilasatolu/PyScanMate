from pyyorozuya.get_files import get_files as gf

def grep(path, keywords):
    grep_result = []
    target_files = gf(path)
    for k in keywords:
        keyword_info = {'keyword': k, 'is_used': False, 'where': []}
        for file in target_files:
            line_count = 0
            file_info = {'file': file, 'line': []}
            try:
                with open(file, encoding = 'UTF-8') as f:
                    for l in f:
                        line_count += 1
                        if k in l:
                            file_info['line'].append(line_count)
                    if len(file_info['line']) > 0:
                        keyword_info['where'].append(file_info)
            except Exception:
                print(file + 'でエラー')
        if len(keyword_info['where']) > 0:
            keyword_info['is_used'] = True
            grep_result.append(keyword_info)
    return grep_result