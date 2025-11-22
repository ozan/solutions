#include "protein_translation.h"
#include <stdint.h>

#define AA_INVALID -1
#define AA_STOP 0

// Static lookup table for direct codon->amino_acid mapping.
// Fully initialized to ensure non-coding codons are AA_INVALID.
static const int amino_acid_table[64] = {
    // Value: -1 = AA_INVALID, 0 = AA_STOP, >0 = amino_acid_t
    /* AAA */ AA_INVALID, /* AAC */ AA_INVALID, /* AAG */ AA_INVALID, /* AAU */ AA_INVALID,
    /* ACA */ AA_INVALID, /* ACC */ AA_INVALID, /* ACG */ AA_INVALID, /* ACU */ AA_INVALID,
    /* AGA */ AA_INVALID, /* AGC */ AA_INVALID, /* AGG */ AA_INVALID, /* AGU */ AA_INVALID,
    /* AUA */ AA_INVALID, /* AUC */ AA_INVALID, /* AUG */ Methionine, /* AUU */ AA_INVALID,
    /* CAA */ AA_INVALID, /* CAC */ AA_INVALID, /* CAG */ AA_INVALID, /* CAU */ AA_INVALID,
    /* CCA */ AA_INVALID, /* CCC */ AA_INVALID, /* CCG */ AA_INVALID, /* CCU */ AA_INVALID,
    /* CGA */ AA_INVALID, /* CGC */ AA_INVALID, /* CGG */ AA_INVALID, /* CGU */ AA_INVALID,
    /* CUA */ AA_INVALID, /* CUC */ AA_INVALID, /* CUG */ AA_INVALID, /* CUU */ AA_INVALID,
    /* GAA */ AA_INVALID, /* GAC */ AA_INVALID, /* GAG */ AA_INVALID, /* GAU */ AA_INVALID,
    /* GCA */ AA_INVALID, /* GCC */ AA_INVALID, /* GCG */ AA_INVALID, /* GCU */ AA_INVALID,
    /* GGA */ AA_INVALID, /* GGC */ AA_INVALID, /* GGG */ AA_INVALID, /* GGU */ AA_INVALID,
    /* GUA */ AA_INVALID, /* GUC */ AA_INVALID, /* GUG */ AA_INVALID, /* GUU */ AA_INVALID,
    /* UAA */ AA_STOP,    /* UAC */ Tyrosine,   /* UAG */ AA_STOP,    /* UAU */ Tyrosine,
    /* UCA */ Serine,     /* UCC */ Serine,     /* UCG */ Serine,     /* UCU */ Serine,
    /* UGA */ AA_STOP,    /* UGC */ Cysteine,   /* UGG */ Tryptophan, /* UGU */ Cysteine,
    /* UUA */ Leucine,    /* UUC */ Phenylalanine, /* UUG */ Leucine, /* UUU */ Phenylalanine,
};


// Maps a single character to a 2-bit value at runtime.
static int c2b(char c) {
  switch (c) {
  case 'A':
    return 0;
  case 'C':
    return 1;
  case 'G':
    return 2;
  case 'U':
    return 3;
  default:
    return 64; // guarantee handled as error
  }
}

/* Translate the first 3 chars of given string to an amino acid, or AA_STOP or
 * AA_INVALID. Now uses a direct, fully-initialized lookup table. */
int trans(const char *s) {
  if (s == NULL)
    return AA_INVALID;

  // Compute lookup index
  int idx = (c2b(s[0]) << 4) + (c2b(s[1]) << 2) + c2b(s[2]);

  if (idx < 0 || idx > 63)
    return AA_INVALID;

  return amino_acid_table[idx];
}

protein_t protein(const char *const rna) {
  protein_t out = {.valid = true, .count = 0};
  const char *s = rna;

  while (*s && out.count < MAX_AMINO_ACIDS) {
    int t = trans(s);
    if (t == AA_STOP)
      break;
    if (t == AA_INVALID) {
      out.valid = 0;
      out.count = 0;
      break;
    }
    out.amino_acids[out.count++] = t;
    s += 3;
  }
  return out;
}
