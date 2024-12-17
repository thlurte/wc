import os
import argparse

parser = argparse.ArgumentParser("Word Counter")
parser.add_argument('-p','--path',help='Path of Text File',required=True)
parser.add_argument('-c','--character',help='Count Characters',action='store_true')


args = vars(parser.parse_args())


# Step - 01: return the number of byters in the file
if args['character']:
    print(os.stat(args['path']).st_size)
