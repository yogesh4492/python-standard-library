""" FIRST STEP: CREATE A PARSER :
Syntax: class argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True) 

Parameters:
prog- name of the program (default=sys.argv[0])
usage- string describes the program usage(default: generated from arguments added to the parser)
description- text to display before the argument help(default: none)
epilog- text to display after the argument help (default: none)
parents- list of ArgumentParser objects whose arguments should also be included
formatter_class- class for customizing the help output
prefix_chars- set of characters that prefix optional arguments (default: ‘-‘)
fromfile_prefix_chars- set of characters that prefix files from which additional arguments should be read (default: None)
argument_default- global default value for arguments (default: None)
conflict_handler- strategy for resolving conflicting optionals (usually unnecessary)
add_help- Add a -h/--help option to the parser (default: True)
allow_abbrev- Allows long options to be abbreviated if the abbreviation is unambiguous. (default: True)
"""

import argparse
parser=argparse.ArgumentParser(description="Create first Parser")


