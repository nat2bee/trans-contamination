#!/usr/local/bin/python


"""
Take all the names from a list of repeated elements and exclude the repeated ones.

Developed (in my case) to use with a list of names from all the species my transcripts 
blasted against in the database, so I could find the contaminants.

Usage = single_entry.py -i <list> -o <output>

Where: 
list = list with all the names from blast (one per line)
output = the name of the output file to save the non repeated names

Options: -h for usage help
"""

import sys, getopt

names = list()


# Check for the arguments, open the inputs and print useful help messages

try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["list=","output="])
except getopt.GetoptError:
    print '\n', '####     Invalid use     ####', '\n'
    print 'Usage = single_entry.py -i <list> -o <output>'
    print 'For help use single_entry.py -h'
    sys.exit(99)
    
for opt, arg in opts:
    if len(arg) < 2 and opt == '-h':
        print '\n', 'Take all the names from a list os repeated elements and exclude the missing and the repeats.', '\n'
        print 'Usage = single_entry.py -i <list> -o <output>'
        print 'Where: list = list with all the names from blast (one per line)'
        print 'output = the name of the output file to save the non repeated names'
        sys.exit()
    elif len(arg) > 2:
        if opt in ("-i", "list"):
            list = open(arg)
        if opt in ("-o", "utput"):
            output = open(arg,"w")
    elif len(arg) < 2:
        print '\n', '###    Arguments are missing   ###', '\n', '\n' 'Use -h option for help\n'
        sys.exit(1)
    else:
        assert False, "unhandled option"



# Open the save each name once in the list and exclude the missing data "-"

for name in list:
    species_name = str(name)
    if species_name not in names:
        names.append(species_name)
# Save the names in the list in the output file    
        output.write(species_name)


output.close()
