from Bio import Phylo
import io

s = '(lobster,(cat,dog),(caterpillar,(elephant,mouse)));'

tree = Phylo.read(io.StringIO(s), 'newick')



Phylo.draw_ascii(tree)

