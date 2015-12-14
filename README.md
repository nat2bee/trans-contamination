# trans-contamination
Scripts used to clean contaminant transcripts from a transcriptome dataset using the annotation data from Annocript and the clusters from Corset.


# single_entry.py
Take all the names from a list of repeated elements and exclude the repeated ones.

Developed (in my case) to use with a list of names from all the species my transcripts 
blasted against in the database, so I could find the contaminants.

Usage = single_entry.py -i <list> -o <output>

Where: 
list = list with all the names from blast (one per line)
output = the name of the output file to save the non repeated names

Options: -h for usage help
