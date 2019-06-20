
typedef struct {
  int key;
  char *value;
} legacy_map;

typedef struct {
  char key;
  int value;
} new_map;

int convert(legacy_map input[], int input_len, new_map *output[]);
