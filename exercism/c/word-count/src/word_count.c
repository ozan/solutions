#include <string.h>

#include "word_count.h"

int word_count(char *input_text, word_count_word_t words[MAX_WORDS]) {
  int n_words = 0, i, found;
  char word[MAX_WORD_LENGTH], *word_p = word, c;

  // copy each string, up to a delimiter, out of input_text
  while (1) {
    c = *input_text++;

    if (c >= 'A' && c <= 'Z')
      c += 32;

    // once finished, compare to each word in words
    if ((c == ' ' || c == ',' || c == '\0') && word != word_p) {
      if (*(word_p - 1) == '\'')
        *(word_p - 1) = '\0'; // remove trailing apostrophe
      *word_p = '\0';
      found = 0;
      for (i = 0; i < n_words; i++) {
        if (strcmp(words[i].text, word) == 0) {
          // if match, increment
          words[i].count++;
          found = 1;
          break;
        }
      }
      if (!found) {
        // else, insert a new word
        strncpy(words[n_words].text, word, MAX_WORD_LENGTH);
        words[n_words].count = 1;
        n_words++;
      }
      word_p = word;
    } else if ((c >= 'a' && c <= 'z') || (c >= '0' && c <= '9') ||
               (c == '\'' && word != word_p)) {
      *word_p++ = c;
    }
    if (c == '\0')
      break;
  }

  return n_words;
}
