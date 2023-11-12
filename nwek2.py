import io
import sys
from Bio import Phylo


f = open('rosalind_nkew (2).txt', 'r')
ps = [i.split('\n') for i in f.read().strip().split('\n\n')]

for i, line in ps:
    x, y = line.split()
    tree = Phylo.read(io.StringIO(i), 'newick')
    sys.stdout.write('%s' % round(tree.distance(x,y)) + ' ')
sys.stdout.write('\n')