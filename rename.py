"""/*=====================================================================
 Program: Program 1
 Author: John Colton, Jessi Thompson
 Class: CSC 461 Programming Languages
 Instructor: Dr. Weiss
 Date: September 22, 2016
 Description: TODO: FILL IN
 Input: 
 Output:
 Compilation instructions:
 Usage:
 Modifications: TODO: FILL IN FROM GITHUB COMMITS
 Date                Comment
 September 6         Look at parsing arguments
 September 7         Set argparse, began to parse arguments into lists
 
"""
import sys, glob, platform, argparse, getopt

#Global variables - try not to use these


# here is the "main" function, must define it before using it
def main( argv ):
    ''' Starts program, checks for correct usage, checks platform, sets global variables
    and begins analysis of files in directory.'''
    
    '''NOTES:
    We can add an action='append' to the attributes of the parser.add_argument to make repeat 
    instances of arguments save to lists of lists.
    
    For example:
    -r a b -r c d
    would be saved
    args.replace = [[a, b], [c, d]]
    
    if we think we want that?
    '''
    
    
    ''' To do: Figure out how to call functions from other modules'''
    
    parser = argparse.ArgumentParser( usage = "-h or --help for full help and usage menu" )
    
    # optional arguments 
    # plain arguments
    parser.add_argument('-v', "--verbose", action="store_true", help="print old and new filenames during processing")
    parser.add_argument('-p', "--print", action="store_true", help="only print old and new filenames, do not rename")
    parser.add_argument('-i', "--interactive", action="store_true", help="interactive mode, ask user prior to processing each file")
    parser.add_argument('-l', '--lower', action="store_true", help='convert filenames to lowercase')
    parser.add_argument('-u', '--upper', action="store_true", help='convert filenames to uppercase')
    parser.add_argument('-d', '--delete', action="store_true", help='delete files')
    parser.add_argument('-dt', '--touch', action="store_true", help='"touch files" (update time/date stamp to current date/time)')
    # arguments with required parameters and potential consecutive calls with their own data
    parser.add_argument('-t', '--trim', type=int, action='append', default=[], help='n > 0: trim n characters from start of each filename. n < 0: trim n characters from the end of each file name')    
    parser.add_argument('-r', '--replace', action='append', nargs=2)
    parser.add_argument('-n', '--number', action='append', nargs=1, metavar=('countstring')) 
    parser.add_argument('-D', '--date', action='append', nargs=1, metavar='DDMMYYYY', type=str, help='change file datestamps')
    parser.add_argument('-T', '--time', action='append', nargs=1, metavar='HHMMSS', type=str, help='change file timestamps')

    # Required arguments - list of filenames
    parser.add_argument("names", type=str, nargs='+', help="list of strings")
    
    # parse command arguments
    args = parser.parse_args()
            
    # Check platform, if not Linux or Windows return 1 from program.
    # pass systemPlatform into funcs that need to differentiate if necessary?
    systemPlatform = setPlatform(platform.system())
    if systemPlatform == 'E':
        print('Platform not recognized by file rename tool. Exiting...')
        return 1
        
    # Parse command line arguments
    '''
     The idea here is to chop up the command line arguments after it encounters a -r, -t, or -n?
    because that would end a sequence of changes - since we're executing consecutive arguments.

    Some special cases...
    In the case of encountering a Delete in a sequence of actions, stop execution there and delete the files listed after the delete
    In the case of encountering a Print in a sequence of actions, stop execution there and just print the file names listed after the print
    '''

    # set some important variables...
    replaceCount = 0
    numberCount = 0
    trimCount = 0
    dateCount = 0
    timeCount = 0
    
    #get a list going for commands and their parameters
    masterExecutionList = []

    # loop through sys.argv, building a list of execution commands, tupled with their parameters
    for cmd in sys.argv:
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
            replaceCount += 1    # keep track of what repeat we've found to do lookup

        elif cmd in ('-n', '--number'):
            masterExecutionList.append(('number', args.number[numberCount]))
            numberCount += 1
            
        elif cmd in ('-D', '--date'):
            masterExecutionList.append(('date', args.date[dateCount]))
            dateCount += 1
        
        elif cmd in ('-T', '--time'):
            masterExecutionList.append(('time', args.time[timeCount]))
            timeCount += 1
            
    
    # Use something like this to loop through the execution list and send the tuple to another function
    count = 0
    for element in masterExecutionList:
        print(masterExecutionList[count])
        count += 1

    
def setPlatform(val):
    '''Checks whether the machine is running Linux or Windows. If it's not running
    Linux or Windows, it throws an error and returns 1'''
    if val == 'Linux':
            return 'L'
    elif val == 'Windows':
            return 'W'
    else:
            return 'E'  # for error


# this pattern must occur after the function definitions (typically at the end of the file)
if __name__ == '__main__':
    main( sys.argv )
