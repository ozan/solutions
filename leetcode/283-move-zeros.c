#include <assert.h>

void moveZeroes(int *nums, int numsSize) {
  int slot = 0;
  for (int i = 0; i < numsSize; i++) {
    int num = nums[i];
    if (num != 0 && i != 0) {
      for (int j = slot; j < i; j++) {
        if (nums[j] == 0) {
          nums[j] = num;
          nums[i] = 0;
          slot = j + 1;
          break;
        }
      }
    }
  }
}

int main(int argc, char const *argv[]) {
  int testVals[] = {0, 1, 0, 3, 12};
  moveZeroes(testVals, 5);
  assert(testVals[0] == 1);
  assert(testVals[1] == 3);
  assert(testVals[2] == 12);
  assert(testVals[3] == 0);
  assert(testVals[4] == 0);
  return 0;
}
