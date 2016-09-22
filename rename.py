#!python3

'''
 Program:       Program 1
 Author:        John Colton and Jessi Thompson
 Class:         CSC 461 Programming Languages
 Instructor:    Dr. Weiss
 Date:          September 22, 2016
 Description:   This program allows the user to rename files in a given
    directory according to certain choices and accompanying parameters as 
    specified in the proram problem statement. Users may do such operations on 
    files such as changing all names to upper or lower case, trim a given number
    of characters from the beginning or end of the end of a filename, replace 
    certain strings found within a filename, and numbering a sequence of files 
    that match a pattern. Additional options include modification of the date
    and time the files were accessed, 'touching' a file, deletion, and a number
    of helpful modes the user may enable. These include the standard help menu,
    a verbose option to print old and new filenames during processing, and an 
    interactive mode to ask the user each time whether they would like to rename
    the current file. In this mode, the user will type in the filename.
    
    The program begins by creating an argparse Argument Parser to allow the 
    program to parse the command line correctly given whatever arguments the
    user provides. The operating system is checked, and a list of the files to 
    be modified is created. If printing or verbose, the program prints the files
    to be modified. If interactive, the system asks the user what they would 
    like the file to be renamed to and then the file goes to be renamed. 
    
    The file modification functions are in modifiers.py. Modifiers.py examines
    the parameters passed in and then creates a lambda function accordingly. 
    Upper, lower, trim and replace are all able to be executed with the in-line
    lambda functions. Countstring, date, time, touch, and delete are all sent to
    the appropriate function in modifiers.py that will do that work.
    
    After modification, the new filenames are printed if verbose is 
    selected.
    
 Input:     Appropriate command-line arguments
 Output:    If user selects verbose, print or interactive optinons, some output 
            will go to terminal
 Usage:     python rename.py [-h] [-l] [-u] [-t n] [-r str1 str2] [-n str]
                    [-v] [-p] [-i] [-d] [-dt] [-D] [-T] listofFiles
 Modifications:
 Date           Comment
 September  2   `rename.py` created.
 September  5   `helpers.py` created and preliminary argument parsing started.
 September  6   `modifiers.py` created with working functions for `upper`,
                `lower`, `trim`, and `replace`. `helpers.py` updated with
                functions for getting, deleting, and touching files, as well as
                functions for parsing input time strings (DDMMYYYY, HHMMSS).
 September  7   Documentation added for functions in `helpers.py`. Set
                `argparse` and began to parse arguments into lists. Argument
                parsing nearly finalized. Main documentation started. Much
                unnecessary code removed. Function to check operating system
                added (in `rename.py`).
 September  8   Many bug fixes, documentation additions, and code reordering.
                Argument parsing finalized. Code to format arguments created.
 September  9   Bug fixes and `countstring` function started.
 September 12   More formatting and documentation. `modify` functions changed
                to be more interchaneable. `countstring` function finished.
 September 13   Bug fixes and file management added.
 September 14   `changeDate` and `changeTime` functions finished.
 September 16   Cleaned up code and updated main documentation.
 September 17   More formatting and cleaning. Added checks for input commands
                and for files existing. Fixed `getFiles()` to not get
                directories. Fixed filename modification loop. Added output
                for `print` and `verbose`. Added interactive mode. Fixed `trim`
                argument parsing. Added loop to actually rename the files.
 September 20   Fixed countstring argument parsing. Fixed `changeDate()`,
                `changeTime()`, `touchFiles()`, and `deleteFiles()` not
                returning anything. Fixed `changeDate()` and `changeTime()`.
 September 21   Documentation completed
'''

import sys, platform, argparse
from os import rename

def main(argv):
    ''' Starts program, checks for correct usage, checks platform, sets global
    variables, and begins analysis of files in directory. '''

    parser = argparse.ArgumentParser(usage = 'python rename.py [-h] [-l] [-u]'\
    ' [-t n] [-r str1 str2] [-n str] [-v] [-p] [-i] [-d] [-dt] [-D] [-T]' \
    ' files')

    # plain arguments
    parser.add_argument('-v', '--verbose', action = 'store_true',
        help = 'print old and new filenames during processing')
    parser.add_argument('-p', '--print', action = 'store_true',
        help = 'only print old and new filenames, do not rename')
    parser.add_argument('-i', '--interactive', action = 'store_true', 
        help = 'interactive mode, ask user prior to processing each file')
    parser.add_argument('-l', '--lower', action = 'store_true', 
        help = 'convert filenames to lowercase')
    parser.add_argument('-u', '--upper', action = 'store_true', 
        help = 'convert filenames to uppercase')
    parser.add_argument('-d', '--delete', action = 'store_true', 
        help = 'delete files')
    parser.add_argument('-dt', '--touch', action = 'store_true',
        help = '`touch` files (update time/date stamp to current date/time)')
        
    # arguments with required parameters, potential consecutive calls 
    parser.add_argument('-t', '--trim', action = 'append', nargs = 1, 
        metavar = 'n', help = 'n > 0: trim n characters from the start of \
        each filename. n < 0: trim n characters from the end of each filename.',
        type = int)
    parser.add_argument('-r', '--replace', action = 'append', nargs = 2, 
        metavar = ('A','B'), help = 'do a regular expression replace on the \
        given filenames. A is old, B is new.')
    parser.add_argument('-n', '--number', action = 'append', nargs = 1,
        metavar = 'countstring', help = 'Given a string with a certain number \
        of hashes, rename files to new string, numbering in order with hashes')
    parser.add_argument('-D', '--date', action = 'append', nargs = 1, 
        metavar = 'DDMMYYYY', help = 'change file modification datestamps')
    parser.add_argument('-T', '--time', action = 'append', nargs = 1,
        metavar = 'HHMMSS', help = 'change file modification timestamps')
    # required arguments
    parser.add_argument('files', type = str, nargs = '+', 
        help = 'list of files to be modified')

    # parse command arguments
    args = parser.parse_args()

    from helpers import setPlatform, makeList, getFiles

    # Check platform, if not Linux or Windows return 1 from program.
    systemPlatform = setPlatform(platform.system())
    if systemPlatform == 'E':
        print('Platform not recognized by file rename tool.')
        return

    # Get a list going for commands and their parameters.
    masterExecutionList = makeList(sys.argv, args)
    if not masterExecutionList and not args.interactive:
        print('You must enter at least one command.')
        return

    files = [] # List of all files that will be modified (including *).
    for file in args.files:
        files += getFiles(file)
    if not files:
        print('None of the files you entered could be found.')
        return

    # Print Original Names
    if args.print or args.verbose:
        print('Input Files:', files)

    # Get new filenames
    import copy, modifiers
    modified = copy.deepcopy(files)
    if args.interactive:
        modified = [input('What would you like to rename `' + file + '` to?\n') for file in modified]
    else: # Loop through the execution list and send the tuple to another fxn.
        for arg, tuple in masterExecutionList:
            if args.print and (arg in ['time', 'date', 'touch', 'delete']):\
                continue
            else: modified = modifiers.modify[arg](modified,tuple)

    # Rename Files
    if not args.print and not args.delete:
        for start, end in zip(files, modified):
            rename(start, end)

    # Print Final Names
    if args.print or args.verbose:
        print('Output Files:', modified)

# "Main"
if __name__ == '__main__':
    main( sys.argv )
