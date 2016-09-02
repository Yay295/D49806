import sys, glob

def indexOf(element, list):
	try: return list.index(element)
	except ValueError: return False

fileargloc = indexOf("-r", sys.argv);
if fileargloc != False:
	fileargloc = indexOf("--replace", sys.argv);
files = {"start": sys.argv[fileargloc+2], "end": sys.argv[fileargloc+3]}

print(glob.glob(sys.argv[0]))
print(files)
