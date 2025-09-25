""" Second Step Is : Adding Argument 
it use add_argument() methods ,it take input from command line

syntax:
ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest]) 

Parameter:
name or flags- either a name or list of option string
action- basic type of action to be taken when this argument is encountered at the command line
nargs- number of command-line arguments that should be consumed
const- constant value required by some action and nargs selections
default- value produced if the arguments are absent from the command line
type- type to which the command line arguments should be converted.
choices - A container of the allowable values for the argument 
required - Whether or not the command-line option may be omitted (optionals only)
help- brief description of what the argument does
metavar - A name for the argument in usage messages
dest - The name of the attribute to be added to the object returned by parse_args()

"""

import argparse
parser=argparse.ArgumentParser(description="With Add Argument methods")

parser.add_argument("echo")#popsitional argument

parser.add_argument("name",help="Enter Your Name")# help statement print
# b=parser.parse_args()
parser.add_argument("Square",type=int,help="Enter A number For return its Square")
# print(b.name)
parser.add_argument("-g","--gdrive_id",required=True,help='enter A gdrive')
a=parser.parse_args()

print(a.echo,a.name,a.Square**2)







