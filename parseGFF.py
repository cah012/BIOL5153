#! /usr/bin/env python3

# load required modules

from Bio import SeqIO
import argparse

# create an ArgumentParser object ('parser') that will hold all the information necessary to parse the command line

parser = argparse.ArgumentParser(description="This script filters out sequences from a FASTA file that are shorter than a user-specified length cutoff")

# use the add_argument() method to add a positional argument
# positional arguments are *required* inputs, so their order/position matters
# argparse treats all options as strings unless told to do otherwise

parser.add_argument("fasta", help="name of FASTA file")

parser.add_argument("gff", help="name of GFF file")

# parse the arguments

args = parser.parse_args()

print("We're gonna open this FASTA file:", args.fasta)

print("We're gonna open this GFF file:", args.gff)

############################ pre-parse code 

from Bio import SeqIO
fasta = SeqIO.read(args.fasta, "fasta")

# read in the genome (FASTA format), store it in a variable - use SeqIO for this

fasta = open("watermelon.fsa").read()

# use this..? ask about it --> fasta = list(SeqIO.parse("watermelon.fsa", "...)

# open the GFF file

gff = open(args.gff)

# read GFF file line by line using a for loop
for line in gff:

# split strings into list based on tabs
	coordinates = line.split("\t")

# define start and end coordinates as integers 
	start = int(coordinates[3]) - 1
	
# add 1 to end so it includes the very last number
	end = int(coordinates[4]) + 1
	
# define organism/species name
	name = (Citrullus_lanatus)
	
# add in actual GFF loop code

	in_file = "watermelon.gff"

	in_handle = open(in_file)
	gff.parse(in_handle, target_lines=1000):
    	print rec

# close the GFF file

	in_handle.close()