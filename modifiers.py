import os, re


def countstring(files, string):
	for i, file in enumerate(files):
		return


def changeDate(files, date):
	for file in files:
		continue

def changeTime(files, time):
	for file in files:
		continue


def touchFiles(files):
	''' man touch '''
	for file in files:
		try:
			pathlib.Path(file).touch()
		except FileExistsError as e:
			print(e)

def deleteFiles(files):
	''' Attempts to delete the files passed in as a list of filenames. '''
	for file in files:
		try:
			os.remove(file)
		except OSError as e:
			print(e)


modify = {
	'upper': lambda files: [filename.upper() for filename in files],
	'lower': lambda files: [filename.lower() for filename in files],
	'trim': lambda files, amount: [(filename[amount if amount >= 0 else 0 : len(filename) if amount >= 0 else len(filename) + amount]) for filename in files],
	'replace': lambda files, before, after: [re.sub(before, after, filename) for filename in files],
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
modify['replace'].__doc__ = ''' Does a RegEx replace on each string in `files`.
`before` is the RegEx replacement string, and `after` is the other RegEx string. 
That's not a very good description actually... '''


# Code for Testing
if __name__ == '__main__':
	test = ['TeSt','ASFSD','thisislowercase']

	print('Original:', test)
	print('UPPERCASE:', modify['upper'](test))
	print('lowercase:', modify['lower'](test))
	print('trim before:', modify['trim'](test, 5))
	print('trim after:', modify['trim'](test, -3))
	print('replace:', modify['replace'](test, '(.*)[Ss]', '\\1'))
	print('countstring:', modify['countstring'](test, 'a##b#c###'))
