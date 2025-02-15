import os
import re

def getFiles(path, reg = r'.*$', hidden = False):
    files = []
    regPtn = re.compile(reg)
    def findFile(path):
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
            fullPath = os.path.join(path, item)
            if os.path.isfile(fullPath):
                if regPtn.search(item):
                    files.append(fullPath)
                continue
            findFile(fullPath)
    findFile(path)
    return files

def formatTxt(strList, beforeReg, after = ""):
    if type(strList) != list and type(strList) == str:
        strList = [strList]
    newList = []
    regPtn = re.compile(beforeReg)
    if len(strList) == 0:
        return newList
    for str in strList:
        newList.append(re.sub(regPtn, after, str))
    return newList

def grep(path, keywords):
    grepResult = []
    targetFiles = getFiles(path)
    for k in keywords:
        keywordInfo = {'keyword': k, 'isUsed': False, 'where': []}
        for file in targetFiles:
            lineCount = 0
            fileInfo = {'file': file, 'line': []}
            try:
                with open(file, encoding = 'UTF-8') as f:
                    for l in f:
                        lineCount += 1
                        if k in l:
                            fileInfo['line'].append(lineCount)
                    if len(fileInfo['line']) > 0:
                        keywordInfo['where'].append(fileInfo)
            except Exception:
                print(file + 'でエラー')
        if len(keywordInfo['where']) > 0:
            keywordInfo['isUsed'] = True
            grepResult.append(keywordInfo)
    return grepResult