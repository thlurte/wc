import os
import argparse
import re

parser = argparse.ArgumentParser("Word Counter")
parser.add_argument('-p','--path',help='Path of Text File',required=True)
parser.add_argument('-c','--character',help='Count Characters',action='store_true')
parser.add_argument('-w','--word',help='Count Words',action='store_true')


args = vars(parser.parse_args())


# Step - 01: return the number of byters in the file
if args['character']:
    print(os.stat(args['path']).st_size)

# Step - 03: return the word count
elif args['word']:
    with open(args['path'],'r') as file:
        print(len(re.split(' |\n|\t',file.read())))
