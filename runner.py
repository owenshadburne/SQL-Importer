import sys
from file_importer import *

if __name__ == '__main__':
    # Call the class and run your code here
    #
    # You can assume that sys.argv[1] is the name
    # of the file to import and that it exists.
    #
    
    i = Importer()
    i.import_file(sys.argv[1])