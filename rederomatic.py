import argparse


def parse_arguments():
    '''
        Input - None
        Output - Command line argument list from ParseArgument object
    '''
    # Parser object
    parser = ParseArgument()
    
    # Command line arguments
    parser.add_argument("-f", "--file", required = True, action = "store_true", help = "Input art file")
    parser.add_argument("-s", "--sizes", required = True, action = "store_true", help = "List of sizes to render in")
    parser.add_argument("-m", "--molds", required = True, action = "store_true", help = "List of mouldings to render in")
    
    # List of arguments from the command line
    args = parser.parse_args()
    
return args


if __name__ == "__main__":
    print("We started at the top and now we're here.")
    
    ### LOCAL VARIABLES ###
    args  # Parsed arguments
    filename = ""  # Input art filename parsed from args
    listOfSizes = []  # List of sizes parsed from args
    listOfMolds = []  # List of moldings parsed from args
    
    ### PARSE CLI ARGUMENTS ###
    args = parse_arguments()
    
    # Filename
    if args.file and args.file.__len__() > 0:
        filename = args.file
    
    # Sizes
    if args.sizes:
        listOfSizes = args.size.split(",")
    
    # Moudlings
    if args.molds:
        listOfMolds = args.molds.split(",")
        
    ### TEST ###
    print("Filename:\t{}".format(filename))  # DEBUGGING
    print("Sizes:   \t{}".format(listOfSizes))  # DEBUGGING
    print("Molds:   \t{}".format(listOfMolds))  # DEBUGGING
        
        
    
    
