#!/usr/bin/env python3

dna=(ACTGTACGTGCACTGATC)

dna = dna.upper()

print(dna)

a_count = dna.count('A')
g_count = dna.count('G')
c_count = dna.count('C')
t_count = dna.count('T')

dna_length = len(dna)
gc = (g_count+c_count)
