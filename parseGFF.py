#! /usr/bin/env python3

# read in the genome (FASTA format), store it in a variable - use SeqIO for this

full_genome = open("watermelon.gff")

# open the GFF file

import pprint
from BCBio.GFF import GFFExaminer

	in_file = "watermelon.gff"
	examiner = GFFExaminer()
	in_handle = open(in_file)
	pprint.pprint(examiner.parent_child_map(in_handle))

# read in a file line by line using a for loop
def get_at_percentage(dnasequence, nt_list=['A','T','G','C']):
	dnasequence = dnasequence.upper()
	sequence_length = len(dnasequence)
	total = 0	
	for nt in nt_list:
		nt = nt.upper()
		at_count = dnasequence.count(nt)
		total = total + at_count
		percentage = total * 100 / sequence_length
		return percentage

# close the GFF file

in_handle.close()