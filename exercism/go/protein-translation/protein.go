package protein

var translations = map[string]string{
	"AUG": "Methionine",
	"UUU": "Phenylalanine",
	"UUC": "Phenylalanine",
	"UUA": "Leucine",
	"UUG": "Leucine",
	"UCU": "Serine",
	"UCC": "Serine",
	"UCA": "Serine",
	"UCG": "Serine",
	"UAU": "Tyrosine",
	"UAC": "Tyrosine",
	"UGU": "Cysteine",
	"UGC": "Cysteine",
	"UGG": "Tryptophan",
	"UAA": "STOP",
	"UAG": "STOP",
	"UGA": "STOP",
}

// FromCodon returns the protein for a given codon
func FromCodon(codon string) string {
	return translations[codon]
}

// FromRNA returns the series of codons from an RNA string
func FromRNA(rna string) (proteins []string) {
	for i := 0; i < len(rna); i += 3 {
		c := FromCodon(rna[i : i+3])
		if c == "STOP" {
			break
		}
		proteins = append(proteins, c)
	}
	return
}
