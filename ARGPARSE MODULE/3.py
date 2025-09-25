""" Third Step : Parsing Argument in second data stored in this step parse_args() method convert 
data into required Type  """

import argparse

parser=argparse.ArgumentParser(description="Heloo Averyone")
parser.add_argument("-g","id",required=True,help="Gdrive folder id ")
args=parser.parse_args()
print(args)