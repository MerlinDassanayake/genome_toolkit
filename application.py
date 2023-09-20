from genome_toolkit import genomeToolkit

# creating an instance of our genomeToolkit class
gt = genomeToolkit()

seq = "AAAGAAAATTGA"
kmer = "AA"

print(gt.count_kmer_regexp(seq, kmer))
