from genome_toolkit import genomeToolkit

# creating an instance of our genomeToolkit class
gt = genomeToolkit()

seq = "acgtgagcaagacgggcttgtggcgaagtacgtcctagttccagggtgctcagttaagttctcgcatgttcaaagtgttatatacaaacagaggaactaa"
kmer = "aa"
k_len = 3

# print(gt.count_kmer_regexp(seq, kmer))
print(gt.find_most_frequent_kmers(seq, k_len))
