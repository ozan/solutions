#include "rna_transcription.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>


static char* key = \
  "................................................................"
  ".U.G...C............A...........................................";

char *to_rna(const char *dna) {
  int i, len = strlen(dna);
  char *rna = (char *)malloc(len + 1);

  for (i = 0; i < len; i++)
    if ((rna[i] = key[(int)dna[i]]) == '.')
      return NULL;

  rna[i] = '\0';
  return rna;
}
