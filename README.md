# trans-contamination
Scripts used to clean contaminant transcripts from a transcriptome dataset using the annotation data from **Annocript** (Musacchia et al. Annocript: a flexible pipeline for the annotation of transcriptomes able to identify putative long noncoding RNAs. Bioinformatics 2015, 31(13):2199-201. doi: 10.1093/bioinformatics/btv106) and the clusters from **Corset** (N. M. Davidson and A. Oshlack. Corset: enabling differential gene expression analysis for de novo assembled transcriptomes. Genome Biology 2014, 15:410  doi:10.1186/s13059-014-0410-6).


# single_entry.py

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


# Find_Contaminant.py

Take a name of species and make a list of all the transcripts blasted with this species

Developed (in my case) to use with the result table from **Annocript** "...filt_ann_out.txt". 
It will make a list of all the transcripts from the possible contaminant species.

**Usage:**
Find_Contaminant.py -i *list* -t *table* -o *output*

**Where:** 
- list = list with all the species name - Taxonomy (one per line)
- output = the name of the output file to save the transcripts from the contaminants
- table = table output from **Annocript** "...filt_ann_out.txt" with the species Taxonomy and transcripts IDs

**Options:** 
-h for usage help


# single_transcriptInCluster.py

Check if all the transcripts from a list have any orthologous based on the **Corset** cluster classification.

Developed (in my case) to check if the transcripts from the list were the only isoform in the gene
cluster resulted from **Corset**. 

**Usage:**
single_transcriptInCluster.py -i *list* -c *cluster* -o *output*

**Where:** 
- list = list with all the transcripts to check (one per line)
- cluster = table result from Corset "...-clusters.txt", where there are the information of clusters and transcripts
- output = the name of the output file to save the transcripts from a cluster with multiple transcripts

The list of all the transcripts Ids that are the only ones in their clusters is also printed in "singles.txt"

**Options:**
-h for usage help

# Find_genes.py

Take a list of genes and find all the transcripts annotated as each gene in you list in the annotation table from **Annocript**.

**Usage:**
Find_genes.py -i *lis*> -a *annotation* -o *output*

**Where:** 
- list = list with all the genes to search for (one per line)
- annotation = table result from Annocript containing the information from annotation (...filt_ann_out.txt)
- output = the name of the output to save the list of transcripts Ids

**Options:**
-h for usage help
