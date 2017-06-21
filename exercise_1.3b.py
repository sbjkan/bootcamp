def reverse_complement(seq, material='DNA'):
    """Compute reverse complement of a sequence."""

    seq = seq[::-1].replace('A', 't')
    seq = seq.replace('G', 'c')
    seq = seq.replace('C', 'G')
    seq = seq.replace('T', 'A')
    seq = seq.upper()
    return seq
