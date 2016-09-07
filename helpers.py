import glob, os, pathlib, time


def getFiles(arg):
	''' Checks that the file(s) passed as a string actually exist, and returns it/them as a list. '''
	if os.path.isFile(arg):
		return [arg]
	else:
		files = glob.glob(arg)
		if len(files) >= 0:
			return files
		else:
			print(file, 'was not found')

def deleteFiles(files):
	''' Attempts to delete the files passed in as a list of filenames. '''
	for file in files:
		try:
			os.remove(file)
		except OSError as e:
			print(e)

def touchFiles(files):
	''' man touch '''
	for file in files:
		try:
			pathlib.Path(file).touch()
		except FileExistsError as e:
			print(e)


def parseDate(string):
	''' Converts a string in the format DDMMYYYY to a format used by the `time` library. '''
	try:
		return time.strptime(string, '%d%m%Y')
	except ValueError as e:
		print e

def parseTime(string):
	''' Converts a string in the format HHMMSS to a format used by the `time` library. '''
	try:
		return time.strptime(string, '%H%M%S')
	except ValueError as e:
		print e
