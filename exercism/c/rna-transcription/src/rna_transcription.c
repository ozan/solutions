#include "rna_transcription.h"
#include <stdlib.h>
#include <string.h>

char *to_rna(const char *dna) {
  int i, len = strlen(dna);
  char *rna = (char *)malloc(len + 1);

  for (i = 0; i < len; i++) {
    switch (dna[i]) {
    case 'G':
      rna[i] = 'C';
      break;
    case 'C':
      rna[i] = 'G';
      break;
    case 'T':
      rna[i] = 'A';
      break;
    case 'A':
      rna[i] = 'U';
      break;
    default:
      return NULL;
    }
  }

  rna[i] = '\0';
  return rna;
}
