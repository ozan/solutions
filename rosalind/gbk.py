from Bio import Entrez

handle = Entrez.esearch(db='nucleotide', term='(Ocyptamus[Organism]) AND ("2006/07/14"[Publication Date] : "2011/05/07"[Publication Date])')
record = Entrez.read(handle)

print(record['Count'])

