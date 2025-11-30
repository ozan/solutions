#include "protein_translation.h"
#include <stdint.h>

#define AA_INVALID 0
#define AA_STOP -1

#define B2(c) ((c) == 'A' ? 0 : ((c) == 'C' ? 1 : ((c) == 'G' ? 2 : ((c) == 'U' ? 3 : 4))))
#define CODON(c1, c2, c3) ((B2(c1) << 4) + (B2(c2) << 2) + B2(c3))

// Static lookup table for direct codon->amino_acid mapping.
// Unspecified codons will be initialized to 0, which is AA_INVALID.
static const signed char amino_acid_table[64] = {
    // Value: 0 = AA_INVALID, -1 = AA_STOP, >0 = amino_acid_t
    [CODON('A', 'U', 'G')] = Methionine,
    [CODON('U', 'U', 'U')] = Phenylalanine,
    [CODON('U', 'U', 'C')] = Phenylalanine,
    [CODON('U', 'U', 'A')] = Leucine,
    [CODON('U', 'U', 'G')] = Leucine,
    [CODON('U', 'C', 'U')] = Serine,
    [CODON('U', 'C', 'C')] = Serine,
    [CODON('U', 'C', 'A')] = Serine,
    [CODON('U', 'C', 'G')] = Serine,
    [CODON('U', 'A', 'U')] = Tyrosine,
    [CODON('U', 'A', 'C')] = Tyrosine,
    [CODON('U', 'G', 'U')] = Cysteine,
    [CODON('U', 'G', 'C')] = Cysteine,
    [CODON('U', 'G', 'G')] = Tryptophan,
    [CODON('U', 'A', 'A')] = AA_STOP,
    [CODON('U', 'A', 'G')] = AA_STOP,
    [CODON('U', 'G', 'A')] = AA_STOP,
};


protein_t protein(const char *const rna) {
  protein_t out = {.valid = true, .count = 0};
  protein_t invalid = {.valid = false, .count = 0};
  const char *s = rna;
  signed char aa;
  int idx;

  while (*s && out.count < MAX_AMINO_ACIDS) {

    // Compute lookup index from codon characters
    idx = CODON(s[0], s[1], s[2]);

    if (idx > 63)
      return invalid;

    aa = amino_acid_table[idx];

    if (aa == AA_STOP)
      break;
    if (aa == AA_INVALID)
      return invalid;

    out.amino_acids[out.count++] = aa;
    s += 3;
  }
  return out;
}
