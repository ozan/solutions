"""
Generating a character table for the given newick format tree

Idea:

    For each nonterminal node in the parsed tree, consider a split
    where all children of that node are 1, others 0
"""

import io

from Bio import Phylo


def ctbl(tree):
    terms = tree.get_terminals()
    terms.sort(key=lambda c: c.name)

    splits = set()

    for node in tree.get_nonterminals():
        incl = set(node.get_terminals())
        if 2 <= len(incl) < len(terms) - 1:
            spl = ''.join('1' if t in incl else '0' for t in terms)
            splits.add(spl)

    for spl in splits:
        print(spl)


sample = '(dog,((elephant,mouse),robot),cat);'
# ctbl(Phylo.read(io.StringIO(sample), 'newick'))

ctbl(Phylo.read('/Users/oz/Downloads/rosalind_ctbl.txt', 'newick'))
