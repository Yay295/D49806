import glob, os, pathlib, time


def getFiles(arg):
	if os.path.isFile(arg):
		return [arg]
	else:
		files = glob.glob(arg)
		if len(files) == 0:
			print(file, 'was not found')
			return False
		else:
			return files

def deleteFiles(files):
	for file in files:
		try:
			os.remove(file)
		except OSError as e:
			print(e)

def touchFiles(files):
	for file in files:
		try:
			pathlib.Path(file).touch()
		except FileExistsError as e:
			print(e)


def parseDate(string):
	try:
		return time.strptime(string, '%d%m%Y')
	except ValueError as e:
		print e

def parseTime(string):
	try:
		return time.strptime(string, '%H%M%S')
	except ValueError as e:
		print e
