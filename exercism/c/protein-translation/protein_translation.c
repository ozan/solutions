#include "protein_translation.h"

#define AA_INVALID -1
#define AA_STOP 0

/* Translate the first 3 chars of given string to an amino acid, or AA_STOP or
 * AA_INVALID Uses switch statements to avoid strcmp */

int trans(const char *s) {
  if (s == NULL)
    return AA_INVALID;

  char a = *s, b = *(s + 1), c = *(s + 2);

  if (a == 'A' && b == 'U' && c == 'G')
    return Methionine;

  if (a != 'U')
    return AA_INVALID; // other than methionine all start U

  switch (b) {
  case 'A':
    switch (c) {
    case 'U':
    case 'C':
      return Tyrosine;
    case 'A':
    case 'G':
      return AA_STOP;
    default:
      return AA_INVALID;
    }
  case 'U':
    switch (c) {
    case 'A':
    case 'G':
      return Leucine;
    case 'U':
    case 'C':
      return Phenylalanine;
    default:
      return AA_INVALID;
    }
  case 'C':
    switch (c) {
    case 'A':
    case 'U':
    case 'C':
    case 'G':
      return Serine;
    default:
      return AA_INVALID;
    }
  case 'G':
    switch (c) {
    case 'U':
    case 'C':
      return Cysteine;
    case 'G':
      return Tryptophan;
    case 'A':
      return AA_STOP;
    default:
      return AA_INVALID;
    }
  }

  // Default case for any other input (like the original return -1)
  return AA_INVALID; // Assuming UNKNOWN is defined as -1 or similar
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
