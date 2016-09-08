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
    
    parser = argparse.ArgumentParser( usage = "-h for help, -v for verbose, -i for int, -f for float" )
    
    # optional switches (may occur in any order)
    parser.add_argument('-v', "--verbose", action="store_true", help="print old and new filenames during processing")
    parser.add_argument('-p', "--print", action="store_true", help="only print old and new filenames, do not rename")
    parser.add_argument('-i', "--interactive", action="store_true", help="interactive mode, ask user prior to processing each file")
    
    # just some optional arguments
    parser.add_argument('-l', '--lower', help='convert filenames to lowercase')
    parser.add_argument('-u', '--upper', help='convert filenames to uppercase')
    parser.add_argument('-d', '--delete', help='delete files')
    parser.add_argument('-dt', '--touch', help='"touch files" (update time/date stamp to current date/time)')
    parser.add_argument('-D', '--date', type=str, help='format: -D/--date DDMMYYYY change file datestamps')
    parser.add_argument('-T', '--time', type=str, help='format: -T/--time HHMMSS change file timestamps')
    
    # trim argument optional, but required positional argument afteward
    parser.add_argument('-t', '--trim', type=int, help='n > 0: trim n characters from start of each filename. n < 0: trim n characters from the end of each file name')
    
    # replace argument optional, but has required two strings at the end 
    parser.add_argument('-r', '--replace', default = [], nargs='+') # replace accepts two string arguments in a list
    
    # number argument optional, but has required two strings at the end
    parser.add_argument('-n', '--number', default = [], nargs='+')  # number accepts two string arguments in a list
    
    # parse command arguments
    args = parser.parse_args()
    
    # Check platform, if not Linux or Windows return 1 from program.
    systemPlatform = setPlatform(platform.system())
    if systemPlatform == 'E':
        print('Platform not recognized by file rename tool. Exiting...')
        return 1
        
    # Parse command line arguments
    
        
        
    
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
