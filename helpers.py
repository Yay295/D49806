import glob, os.path, time


def getFiles(arg):
	''' Checks that the file(s) passed as a string actually exist, and returns it/them as a list. '''
	if os.path.isfile(arg):
		return [arg]
	else:
		files = glob.glob(arg)
	if len(files) >= 0:
		return files
	else:
		print(file, 'was not found')
		return []


def parseDate(string):
	''' Converts a string in the format DDMMYYYY to a format used by the `time` library. '''
	try:
		return time.strptime(string, '%d%m%Y')
	except ValueError as e:
		print(e)

def parseTime(string):
	''' Converts a string in the format HHMMSS to a format used by the `time` library. '''
	try:
		return time.strptime(string, '%H%M%S')
	except ValueError as e:
		print(e)


def setPlatform(val):
	''' Checks whether the machine is running Linux or Windows. If it's not running
	Linux or Windows, it returns 'E' for "Error". '''
	if val == 'Linux':
		return 'L'
	elif val == 'Windows':
		return 'W'
	else:
		return 'E'


def makeList(argv, args):
	''' Converts the arguments given to this program into a formatted list for easier execution. '''
	masterExecutionList = []
	# set some important variables...
	replaceCount = 0
	numberCount = 0
	trimCount = 0
	dateCount = 0
	timeCount = 0

	# loop through sys.argv, building a list of execution commands, tupled with their parameters
	for cmd in argv:
		if cmd in ('-l', '--lower'):
			masterExecutionList.append(('lower', None))

		elif cmd in ('-u', '--upper'):
			masterExecutionList.append(('upper', None))

		elif cmd in ('-p', '--print'):
			masterExecutionList.append(('print', None))

		elif cmd in ('-d', '--delete'):
			masterExecutionList.append(('delete', None))

		elif cmd in ('-dt', '--touch'):
			masterExecutionList.append(('touch', None))

		elif cmd in ('-t', '--trim'):
			masterExecutionList.append(('trim', args.trim[trimCount]))
			trimCount += 1

		elif cmd in ('-r', '--replace'):
			masterExecutionList.append(('replace', args.replace[replaceCount])) # append execution list with tuple
			replaceCount += 1 # keep track of what repeat we've found to do lookup

		elif cmd in ('-n', '--number'):
			masterExecutionList.append(('number', args.number[numberCount]))
			numberCount += 1

		elif cmd in ('-D', '--date'):
			masterExecutionList.append(('date', args.date[dateCount]))
			dateCount += 1

		elif cmd in ('-T', '--time'):
			masterExecutionList.append(('time', args.time[timeCount]))
			timeCount += 1

	print(masterExecutionList[1][1])

	return masterExecutionList
