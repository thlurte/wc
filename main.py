import argparse

parser = argparse.ArgumentParser("Word Counter")
parser.add_argument('-p','--path',help='Path of Text File',required=True)
parser.add_argument('-c','--character',help='Count Characters',action='store_true')


args = vars(parser.parse_args())

if args['character']:
    with open(args['path'],'r') as file:
        print(file.read())

