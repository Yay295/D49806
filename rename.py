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
import sys, glob, platform, argparse, getopt, os

#Global variables - try not to use these


# here is the "main" function, must define it before using it
def main( argv ):
    ''' Starts program, checks for correct usage, checks platform, sets global variables
    and begins analysis of files in directory.'''

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
    parser.add_argument('-n', '--number', action='append', nargs=1, metavar='countstring') 
    parser.add_argument('-D', '--date', action='append', nargs=1, metavar='DDMMYYYY', type=str, help='change file datestamps')
    parser.add_argument('-T', '--time', action='append', nargs=1, metavar='HHMMSS', type=str, help='change file timestamps')

    # Required arguments - list of filenames
    parser.add_argument("files", type=str, nargs='+', help="list of files to be modified")
    
    # parse command arguments
    args = parser.parse_args()
            
    # Check platform, if not Linux or Windows return 1 from program.
    
    from helpers import setPlatform, makeList, getFiles
    systemPlatform = setPlatform(platform.system())
    if systemPlatform == 'E':
        print('Platform not recognized by file rename tool. Exiting...')
        return 1
    
    #get a list going for commands and their parameters
    masterExecutionList = []
    masterExecutionList = makeList(sys.argv, args)              
    
    print('files list: ', args.files)
    
    files = [] #what we append to, list of all files that will be modified (including *)
    fileCount = 0   
    for element in args.files:
        files += getFiles(args.files[fileCount])
        fileCount += 1
    
    import modifiers
    # Use something like this to loop through the execution list and send the tuple to another function
    modified = []
    for element in masterExecutionList:
        modified = modifiers.modify[element[0]](files,element[1])
    
    # Loop through both lists and rename files, checking for verbose and interactive flags
    for origFile, newFile in zip(files, modified):
        print('original filename: ' , origFile, ' and new filename: ' , newFile)
        if args.interactive:
            response = intput('Do you want to rename ', origFile, ' to ', newFile, '? (y or n)')
            if response.lower() == 'y':
                os.rename(origFile, newFile)
            elif reponse.lower() == 'yes':
                os.rename(origFile,newFile)
            elif response.lower() == 'n':
                print ('Skipping ', origfile)
            elif response.lower() == 'no':
                print('Skipping ', origFile)
            
        elif args.verbose:
            print('Renaming ' , origFile, ' to ', newFile)
            os.rename(origFile, newFile)
        
        else:
            os.rename(origFile, newFile)
            
    #print('files list: ', modified)

# this pattern must occur after the function definitions (typically at the end of the file)
if __name__ == '__main__':
    main( sys.argv )
