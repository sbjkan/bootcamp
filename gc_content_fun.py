seq = 'AACGTGCTAGCTACGGCGCGCGCTACGATCTCATCAAG'

# Initialize the GC counter
n_gc = 0

# Loop through the sequences and count G's and C's
# for means forward loop
# the name "base" refers to what is left from seq after each count
for i, base in enumerate(seq):
    if base in 'GCgc':
        n_gc += 1

print(n_gc / len(seq))
