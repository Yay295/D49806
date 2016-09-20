#!python3

import os, pathlib, re
from time import localtime, mktime
from helpers import parseDate, parseTime


def countstring(files, string):
    ''' Replaces all filenames in `files` with the given string,
    and then replaces all occurences of `#`s in the string with
    a 0-padded number equal to the index of the filename in `files`.
    This returns a new list; it does not modify `files`. '''
    temp = [string] * len(files)
    matches = re.findall('#+', string)
    for i in range(len(files)):
        for match in matches:
            temp[i] = temp[i].replace(match, str(i+1).zfill(len(match)), 1)
    return temp


def changeDate(files, date):
    ''' Changes the day, month, and year of the modification time
    of every file in `files`. '''
    date = parseDate(date)
    for file in files:
        mTime = localtime(os.path.getmtime(file))
        mTime = (date.tm_year, date.tm_mon, date.tm_mday, mTime.tm_hour, mTime.tm_min, mTime.tm_sec, mTime.tm_wday, mTime.tm_yday, mTime.tm_isdst)
        os.utime(file, (os.path.getatime(file), mktime(mTime)))
    return files

def changeTime(files, time):
    ''' Changes the hours, minutes, and seconds of the modification time
    of every file in `files`. '''
    time = parseTime(time)
    for file in files:
        mTime = localtime(os.path.getmtime(file))
        mTime = (mTime.tm_year, mTime.tm_mon, mTime.tm_mday, time.tm_hour, time.tm_min, time.tm_sec, mTime.tm_wday, mTime.tm_yday, mTime.tm_isdst)
        os.utime(file, (os.path.getatime(file), mktime(mTime)))
    return files


def touchFiles(files, dummy):
    ''' Updates the modification time of every file in `files` with the current
    time. Creates the file if it doesn't exist. '''
    for file in files:
        try:
            pathlib.Path(file).touch()
        except FileExistsError as e:
            print(e)
    return files

def deleteFiles(files, dummy):
    ''' Attempts to delete the files passed in as a list of filenames. '''
    for file in files:
        try:
            os.remove(file)
        except OSError as e:
            print(e)
    return files


modify = {
    'upper': lambda files, dummy: [filename.upper() for filename in files],
    'lower': lambda files, dummy: [filename.lower() for filename in files],
    'trim': lambda files, amount: [(filename[amount if amount >= 0 else 0 : len(filename) if amount >= 0 else len(filename) + amount]) for filename in files],
    'replace': lambda files, args: [re.sub(args[0], args[1], filename) for filename in files],
    'countstring': countstring,
    'date': changeDate,
    'time': changeTime,
    'touch': touchFiles,
    'delete': deleteFiles
}


# Add docstrings to lambdas.
modify['upper'].__doc__ = ''' Converts a list of strings to uppercase. '''
modify['lower'].__doc__ = ''' Converts a list of strings to lowercase. '''
modify['trim'].__doc__ = ''' Trims `amount` number of characters from each string in `files`.
If `amount` is positive it trims from the start, otherwise it trims from the end. '''
modify['replace'].__doc__ = ''' Does a RegEx replace on each string in `files`. '''


# Code for Testing
if __name__ == '__main__':
    test = ['TeSt','ASFSD','thisislowercase']

    print('Original:', test)
    print('UPPERCASE:', modify['upper'](test, None))
    print('lowercase:', modify['lower'](test, None))
    print('trim before:', modify['trim'](test, 5))
    print('trim after:', modify['trim'](test, -3))
    print('replace:', modify['replace'](test, ['(.*?)[Ss]', '\\1']))
    print('countstring:', modify['countstring'](test, 'A##BB#CCC###'))
