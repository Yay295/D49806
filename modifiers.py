import re

modify = {
	'upper': lambda files: list(map(lambda filename: filename.upper(), files)),
	'lower': lambda files: list(map(lambda filename: filename.lower(), files)),
	'trim': lambda files, amount: list(map(lambda filename: filename[amount if amount >= 0 else 0 : len(filename) if amount >= 0 else len(filename) + amount], files)),
	'replace': lambda files, before, after: list(map(lambda filename: re.sub(before, after, filename), files))
}

# Code for Testing
if __name__ == '__main__':
	test = ['TeSt','ASFSD','thisislowercase']

	print('Original:', test)
	print('UPPERCASE:', modify['upper'](test))
	print('lowercase:', modify['lower'](test))
	print('trim before:', modify['trim'](test, 5))
	print('trim after:', modify['trim'](test, -3))
	print('replace:', modify['replace'](test, '(.*)S', '\\1'))
