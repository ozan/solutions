package strand

const lookup = "................................................................" +
	".U.G...C............A..........................................."

// ToRNA transcribes dna to rna
func ToRNA(dna string) string {
	rna := make([]byte, len(dna))
	for i := 0; i < len(dna); i++ {
		rna[i] = lookup[dna[i]]
	}
	return string(rna)
}
