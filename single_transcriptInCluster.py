#!/usr/local/bin/python


"""
Check if all the transcripts from a list have any orthologous based on the Corset cluster classification.

Developed (in my case) to check if the transcripts from the list were the only isoform in the gene
cluster resulted from Corset. 

Usage = single_transcriptInCluster.py -i <list> -c <cluster> -o <output>

Where: 
list = list with all the transcripts to check (one per line)
cluster = table result from Corset "...-clusters.txt", where there are the information of clusters and transcripts
output = the name of the output file to save the transcripts from a cluster with multiple transcripts

The list of all the transcripts Ids that are the only ones in their clusters is also printed in "singles.txt"

Options: -h for usage help
"""

import sys, getopt

# Check for the arguments, open the inputs and print useful help messages

try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:c:o:",["list=","cluster=","output="])
except getopt.GetoptError:
    print '\n', '####     Invalid use     ####', '\n'
    print 'Usage = single_transcriptInCluster.py -i <list> -c <cluster> -o <output>'
    print 'For help use single_transcriptInCluster.py -h'
    sys.exit(99)
    
for opt, arg in opts:
    if len(arg) < 3 and opt == '-h':
        print '\n', 'Check if all the transcripts from a list have any orthologous based on the Corset cluster classification.', '\n'
        print 'Usage = single_transcriptInCluster.py -i <list> -c <cluster> -o <output>'
        print 'Where: list = list with all the transcripts to check (one per line)'
        print 'cluster = table result from Corset "...-clusters.txt", where there are the information of clusters and transcripts'
        print 'output = the name of the output file to save the transcripts from a cluster with multiple transcrips'
        sys.exit()
    elif len(arg) > 3:
        if opt in ("-i", "--list"):
            list = open(arg)
        if opt in ("-c", "--cluster"):
            clusters_table = open(arg)
        if opt in ("-o", "--output"):
            output = open(arg,"w")
    elif len(arg) < 3:
        print '\n', '###    Arguments are missing   ###', '\n', '\n' 'Use -h option for help\n'
        sys.exit(1)
    else:
        assert False, "unhandled option"
        
        
# creating variables        
cluster_list = []
isoform_list = []
clusters_dict = dict()




# Read the cluster table and save in a list all the clusters with more then one transcript

for line in clusters_table:
	data = line.split("\t")
	trans_id = data[0]
	cluster_id = data[1]
	cluster_id = cluster_id.rsplit("\n")
	cluster_id = cluster_id[0]
	# Create a dictionary with all the transcripts/clusters
	clusters_dict[trans_id] = cluster_id
	# Use only the cluster prefix to check for multiple isoforms
	prefix = cluster_id.rsplit(".")
	striped_cluster = prefix[0]
	if striped_cluster not in cluster_list:
		cluster_list.append(striped_cluster)
	else:
		isoform_list.append(cluster_id)
		
# Read the transcripts list and check the cluster they belong to. 

out_name = "singles.txt"
singles = open(out_name,"w")

for transcripts in list:
    id = transcripts.rsplit("\n")
    id = id[0]
    cluster = clusters_dict[id]
    if cluster in isoform_list:
	    output.write(id)
	    output.write("\t")
	    output.write(cluster)
	    output.write("\n")
    else: 
        singles.write(id)
        singles.write("\n") 
        
output.close()
singles.close()
