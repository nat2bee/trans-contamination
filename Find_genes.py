#!/usr/local/bin/python


"""
Take a list of genes and find all the transcripts annotated as each gene in you list in 
the annotation table.


Usage = Find_genes.py -i <list> -a <annotation> -o <output>

Where: 
list = list with all the genes to search for (one per line)
output = the name of the output to save the list of transcripts Ids
annotation = table result from Annocript containing the information from annotation (...filt_ann_out.txt)

Options: -h for usage help
"""

import sys, getopt

# Check for the arguments, open the inputs and print useful help messages

try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:a:o:",["list=","annotation","output="])
except getopt.GetoptError:
    print '\n', '####     Invalid use     ####', '\n'
    print 'Usage = Find_genes.py -i <list> -a <annotation> -o <output>'
    print 'For help use Find_genes.py -h'
    sys.exit(99)
    
for opt, arg in opts:
    if len(arg) < 3 and opt == '-h':
        print '\n', 'Take a list of genes and find all the transcripts annotated as each gene in you list in the annotation table.', '\n'
        print 'Usage = Find_genes.py -i <list> -a <annotation> -o <output>'
        print 'Where: list = list with all the genes to search for (one per line)'
        print 'output =  the name of the output to save the list of transcripts Ids'
        print 'annotation = table result from Annocript containing the information from annotation (...filt_ann_out.txt)'
        sys.exit()
    elif len(arg) > 3:
        if opt in ("-i", "--list"):
            list = open(arg)
        if opt in ("-a", "--annotation"):
            annotation = open(arg)
        if opt in ("-o", "--output"):
            output = open(arg,"w")
    elif len(arg) < 3:
        print '\n', '###    Arguments are missing   ###', '\n', '\n' 'Use -h option for help\n'
        sys.exit(1)
    else:
        assert False, "unhandled option"


gene_list = []


# Open the list of genes and save them in a list

for gene in list:
    gene_name = gene.split("\n")
    gene_name = gene_name[0]
    gene_list.append(gene_name)
    

# Check if the GO is in the annotation table line, if so save the transcript Id

for line in annotation:
    elements = line.split("\t")
    transcript_id = elements[1]
    for gene in gene_list:
        if gene in line:
            output.write(transcript_id)
            output.write("\n")
    

output.close()
