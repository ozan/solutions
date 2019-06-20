#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_OUT 100

struct rule {
  char *prefix;
  char isvowel;
};

struct rule rules[] = {
    {"ch", 0},  {"qu", 0}, {"squ", 0}, {"thr", 0}, {"th", 0},
    {"sch", 0}, {"rh", 0}, {"yt", 1},  {"xr", 1},  {"a", 1},
    {"e", 1},   {"i", 1},  {"o", 1},   {"u", 1},
};

struct rule consonant = {".", 0};

int nrules = sizeof(rules) / sizeof(struct rule);

void rotate(char *out, const char *word, int n) {
  int i, len = strlen(word);
  for (i = 0; i < len; i++)
    out[i < n ? len - n + i : i - n] = word[i];
  out[len] = '\0';
}

char *translate(const char *phrase) {
  char rotated[MAX_OUT], *token, *string, *tofree, *out,
      *translated = malloc(MAX_OUT);
  struct rule *rule;

  out = translated;
  tofree = string = strdup(phrase);

  // For each space-delimited token in the string...
  while ((token = strsep(&string, " "))) {
    rule = NULL;

    // Find the first rule that applies, by matching against the token prefix
    for (int i = 0; i < nrules; i++) {
      if (strncmp(rules[i].prefix, token, strlen(rules[i].prefix)) == 0) {
        rule = &rules[i];
        break;
      }
    }

    // If no matching rule, it is a consonant
    if (rule == NULL)
      rule = &consonant;

    // Apply the rule
    if (rule->isvowel) {
      out += sprintf(out, "%say", token);
    } else {
      rotate(rotated, token, strlen(rule->prefix));
      out += snprintf(out, MAX_OUT, "%say", rotated);
    }

    // If the string has more tokens, space out our output
    if (string)
      *out++ = ' ';
  }

  free(tofree);
  return translated;
}

