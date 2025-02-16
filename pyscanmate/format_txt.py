import re

def format_txt(str_list, before_reg, after = ""):
    if type(str_list) != list and type(str_list) == str:
        str_list = [str_list]
    new_list = []
    reg_ptn = re.compile(before_reg)
    if len(str_list) == 0:
        return new_list
    for str in str_list:
        new_list.append(re.sub(reg_ptn, after, str))
    return new_list