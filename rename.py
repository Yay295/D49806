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

#Global variables
platform

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

   # #   # print results of parsing
   #  print( 'command line args:', sys.argv )
   #  print( 'argparse:', args )
   #  print( 'args.verbose =', args.verbose )
   #  print( 'args.print =', args.print )
   #  print( 'args.interactive =', args.interactive )
   #  print( 'args.trim =', args.trim)
   #  print( 'args.replace =', args.replace)
   #  print( 'args.number =', args.number)
    
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
