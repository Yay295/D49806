import sys, glob, platform, argparse, getopt

# Using a "main" function in Python
# CSC461 Programming Languages, Fall 2016 (JMW)
# Main file for Program 1

#Global variables
platform
helpToggle = False
verboseToggle = False
printToggle = False
interactiveToggle = False

# here is the "main" function, must define it before using it
def main( argv ):
    ''' Starts program, checks for correct usage, checks platform, sets global variables
    and begins analysis of files in directory.'''
    
    # check for correct number of command line arguments, parse parameters
    parser = argparse.ArgumentParser(description='Parse the command line arguments!')
    parser.add_argument('-l', '--lower')
    parser.add_argument('-u', '--upper')
    
    parser.add_argument('-v', '--verbose', help='print old and new filenames during processing', action = "store_true")
    parser.add_argument('-i', '--interactive', help='interactive mode, ask user prior to processing each file')
    parser.add_argument('-d', '--delete', help= 'delete files')
    parser.add_argument('-dt', '--touch', help = 'update date/time stamp to current date/time')
    
    # Check platform, if not Linux or Windows return.
    if setPlatform(platform.system()) != 0:
        return 1
        
    
def setPlatform(val):
    '''Checks whether the machine is running Linux or Windows. If it's not running
    Linux or Windows, it throws an error and returns 1'''
    if val == 'Linux':
            global platform
            platform = 'L'
            return 0
    elif val == 'Windows':
            global platform
            platform = 'W'
            return 0
    else:
            print('Platform not recognized for tool. Exiting...')
            return 1 #for error


def usage():
    '''This prints correct usage for the program and possible options, along with their definitions.'''
    print ('This is a file rename utility. Acceptable usage:\n\trename.py options file1 file2... \n\tAvailable Options include:')
    print('\t-l,   --lower    Convert filenames to lowercase')
    print('\t-u,   --upper    Convert filenames to uppercase')
    print('\t-t n, -- trim n  Positive n: trim n characters from the start of each filename')
    print('\t\t\t\t\t   Negative n: trim n characters from the end of each filename')
    print('\t-r "oldstring" "newstring", --replace "oldstring" "newstring"\n\t\t\t\t\t\tReplace oldstring with newstring in filenames')
    print('\t-n countstring, --number countstring\n\t\t\t\t\t\tRename files in sequence using countstring')
    print('\t-D DDMMYYYY, --date DDMMYYYY\tchange file datestamps')
    print('\t-T HHMMSS, --time HHMMSS\t change file timestamps')


# this pattern must occur after the function definitions (typically at the end of the file)
if __name__ == '__main__':
    main( sys.argv )
