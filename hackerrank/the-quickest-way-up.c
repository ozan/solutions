#include <stdio.h>

#define BOARD_SIZE 100

int min_rolls(int *edges) {
  int depth_q[BOARD_SIZE] = {0};
  int val_q[BOARD_SIZE] = {0};
  int seen[BOARD_SIZE + 1] = {0};
  val_q[0] = 1;
  depth_q[0] = 0;
  int rp = 0, wp = 1;
  while (rp < wp) {
    int depth = depth_q[rp];
    int val = val_q[rp];

    if (val == BOARD_SIZE)
      return depth;
    rp++;

    for (int roll = 6; roll > 0; roll--) {
      int next = val + roll;
      if (next > BOARD_SIZE)
        continue;
      if (edges[next])
        next = edges[next];
      if (seen[next])
        continue;
      seen[next] = 1;
      val_q[wp] = next;
      depth_q[wp] = depth + 1;
      wp++;
    }
  }
  return -1;
}

int main() {
  int t, n, a, b;
  scanf("%d", &t);
  while (t--) {
    int edges[BOARD_SIZE + 1] = {0};

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
      scanf("%d %d", &a, &b);
      edges[a] = b;
    }

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
      scanf("%d %d", &a, &b);
      edges[a] = b;
    }

    printf("%d\n", min_rolls(edges));
  }
  return 0;
}
