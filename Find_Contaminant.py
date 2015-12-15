#!/usr/local/bin/python


"""
Take a name of species and make a list of all the transcripts blasted with this species

Developed (in my case) to use with the result table from Annocript "...filt_ann_out.txt". 
It will make a list of all the transcripts from the possible contaminant species.

Usage = Find_Contaminant.py -i <list> -t <table> -o <output>

Where: 
list = list with all the species name - Taxonomy (one per line)
output = the name of the output file to save the transcripts from the contaminants
table = table output from Annocript "...filt_ann_out.txt" with the species Taxonomy and transcripts IDs

Options: -h for usage help
"""

import sys, getopt


# Check for the arguments, open the inputs and print useful help messages

try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:t:o:",["list=","table=","output="])
except getopt.GetoptError:
    print '\n', '####     Invalid use     ####', '\n'
    print 'Usage = Find_Contaminant.py -i <list> -t <table> -o <output>'
    print 'For help use Find_Contaminant.py -h'
    sys.exit(99)
    
for opt, arg in opts:
    if len(arg) < 3 and opt == '-h':
        print '\n', 'Take a name of species and make a list of all the transcripts blasted with this species.', '\n'
        print 'Usage = Find_Contaminant.py -i <list> -o <output>'
        print 'Where: list = list with all the species name - Taxonomy (one per line)'
        print 'table = table output from Annocript "...filt_ann_out.txt" with the species Taxonomy and transcripts IDs'
        print 'output = the name of the output file to save the transcripts from the contaminants'
        sys.exit()
    elif len(arg) > 3:
        if opt in ("-i", "--list"):
            list = open(arg)
        if opt in ("-t", "--table"):
            table = open(arg)
        if opt in ("-o", "--output"):
            output = open(arg,"w")
    elif len(arg) < 3:
        print '\n', '###    Arguments are missing   ###', '\n', '\n' 'Use -h option for help\n'
        sys.exit(1)
    else:
        assert False, "unhandled option"

species_name = ""    
s_name = ""
species_list = []
    

# Take each species name of the list
for name in list:
    species_name = name.split("\n")
    species_name = str(species_name[0])
    species_list.append(species_name)


# Check in each row of the table if this name appears
for line in table:
    split_line = line.split("\t")
    s_name = str(split_line[26])
    if s_name in species_list:
    # Take the transcript ID and save it in the output
        id = split_line[0]
        output.write(id)
        output.write("\n")

output.close()
    
