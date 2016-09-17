#!python3

'''
 Program:       Program 1
 Author:        John Colton and Jessi Thompson
 Class:         CSC 461 Programming Languages
 Instructor:    Dr. Weiss
 Date:          September 22, 2016
 Description:   TODO: FILL IN
 Input:
 Output:
 Usage:
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
 September 17   More formatting and cleaning.
'''

import sys, platform, argparse

def main(argv):
    ''' Starts program, checks for correct usage, checks platform, sets global
    variables, and begins analysis of files in directory. '''

    parser = argparse.ArgumentParser(usage = '-h or --help for full help and usage menu')

    # plain arguments
    parser.add_argument('-v', '--verbose',     action='store_true', help='print old and new filenames during processing')
    parser.add_argument('-p', '--print',       action='store_true', help='only print old and new filenames, do not rename')
    parser.add_argument('-i', '--interactive', action='store_true', help='interactive mode, ask user prior to processing each file')
    parser.add_argument('-l', '--lower',       action='store_true', help='convert filenames to lowercase')
    parser.add_argument('-u', '--upper',       action='store_true', help='convert filenames to uppercase')
    parser.add_argument('-d', '--delete',      action='store_true', help='delete files')
    parser.add_argument('-dt', '--touch',      action='store_true', help='`touch` files (update time/date stamp to current date/time)')
    # arguments with required parameters and potential consecutive calls with their own data
    parser.add_argument('-t', '--trim',    action='append', nargs=1, metavar='n',           help='n > 0: trim n characters from the start of each filename. n < 0: trim n characters from the end of each filename.', type=int)
    parser.add_argument('-r', '--replace', action='append', nargs=2, metavar=('A','B'),     help='do a regular expression replace on the given filenames')
    parser.add_argument('-n', '--number',  action='append', nargs=1, metavar='countstring', help='', type=int)
    parser.add_argument('-D', '--date',    action='append', nargs=1, metavar='DDMMYYYY',    help='change file modification datestamps')
    parser.add_argument('-T', '--time',    action='append', nargs=1, metavar='HHMMSS',      help='change file modification timestamps')
    # required arguments
    parser.add_argument('files', type=str, nargs='+', help='list of files to be modified')

    # parse command arguments
    args = parser.parse_args()

    from helpers import setPlatform, makeList, getFiles

    # Check platform, if not Linux or Windows return 1 from program.
    systemPlatform = setPlatform(platform.system())
    if systemPlatform == 'E':
        print('Platform not recognized by file rename tool. Exiting...')
        return

    # Get a list going for commands and their parameters.
    masterExecutionList = makeList(sys.argv, args)
    if not masterExecutionList:
        print('You must enter at least one command.')
        return

    print('arguments: ', args)
    print('files list: ', args.files)

    files = [] # What we append to. List of all files that will be modified (including *).
    for file in args.files:
        files += getFiles(file)

    import modifiers
    # Use something like this to loop through the execution list and send the tuple to another function
    for element in masterExecutionList:
        modified = modifiers.modify[element[0]](files,element[1])

    print('files list: ', modified)

# this pattern must occur after the function definitions (typically at the end of the file)
if __name__ == '__main__':
    main( sys.argv )
