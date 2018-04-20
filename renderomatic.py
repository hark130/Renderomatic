from argparse import ArgumentParser
import os


def parse_arguments():
    '''
        Input - None
        Output - Command line argument list from ArgumentParser object
    '''
    # Parser object
    parser = ArgumentParser()
    
    # Command line arguments
    parser.add_argument("-f", "--file", type = str, required = True, help = "Input art file")
    parser.add_argument("-s", "--sizes", type = str, required = True, help = "List of sizes to render in")
    parser.add_argument("-m", "--molds", type = str, required = True, help = "List of mouldings to render in")
    
    # List of arguments from the command line
    args = parser.parse_args()
    
    return args


if __name__ == "__main__":
    ### LOCAL VARIABLES ###
    # Parsed arguments
    listOfNames = []  # Input art filenames parsed from args
    listOfSizes = []  # List of sizes parsed from args
    listOfMolds = []  # List of moldings parsed from args
    success = True  # Make this False if anything fails
    
    ### PARSE CLI ARGUMENTS ###
    args = parse_arguments()  # Parsed arguments
    
    # Filenames
    if args.file and args.file.__len__() > 0:
        listOfNames = args.file.split(",")
    
    # Sizes
    if args.sizes:
        listOfSizes = args.sizes.split(",")
    
    # Moudlings
    if args.molds:
        listOfMolds = args.molds.split(",")

    ### INPUT VALIDATION ###
    # Filenames
    if success:
        for filename in listOfNames:
            if filename.__len__() == 0:
                print("Renderomatic detected an empty filename.\nDid include an extra comma in the -f argument?")
                success = False
                break
            elif not os.path.isfile(filename):
                print("Renderomatic was unable to locate file '{}' in '{}'.\nWill you please verify the file exists and that its name was type properly?".format(filename, os.getcwd()))
                success = False
                break
    
    # Sizes
    if success:
        for size in listOfSizes:
            if size.__len__() == 0:
                print("Renderomatic detected an empty size.\nDid include an extra comma in the -s argument?")
                success = False
                break

    # Mouldings
    if success:
        for mold in listOfMolds:
            if mold.__len__() == 0:
                print("Renderomatic detected an empty moulding.\nDid include an extra comma in the -m argument?")
                success = False
                break
        
    ### TEST ###
    print("Filename:\t{}".format(listOfNames))  # DEBUGGING
    print("Sizes:   \t{}".format(listOfSizes))  # DEBUGGING
    print("Molds:   \t{}".format(listOfMolds))  # DEBUGGING
        
        
    
    
