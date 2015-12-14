# trans-contamination
Scripts used to clean contaminant transcripts from a transcriptome dataset using the annotation data from **Annocript** (Musacchia et al. Annocript: a flexible pipeline for the annotation of transcriptomes able to identify putative long noncoding RNAs. Bioinformatics 2015, 31(13):2199-201. doi: 10.1093/bioinformatics/btv106) and the clusters from **Corset** (N. M. Davidson and A. Oshlack. Corset: enabling differential gene expression analysis for de novo assembled transcriptomes. Genome Biology 2014, 15:410  doi:10.1186/s13059-014-0410-6).


- # single_entry.py
Take all the names from a list of repeated elements and exclude the repeated ones.

Developed (in my case) to use with a list of names from all the species my transcripts 
blasted against in the database, so I could find the contaminants.

**Usage:** 
single_entry.py -i *list* -o *output*

**Where:** 
- list = list with all the names from blast (one per line)
- output = the name of the output file to save the non repeated names

**Options:**
-h for usage help
