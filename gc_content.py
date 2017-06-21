try:
    import gc_content
    gave_gc = True
except ImportError as e:
    have_gc = False
finally:
    #Do whatever is necessary like closing files. Pass means do nothing.
    pass

seq = 'AGCAGCGTACGATGCAGATGACGT'

if have_gc:
    print(gc_content.gc(seq))
else:
    print(seq.count('G') + seq.count('C'))
