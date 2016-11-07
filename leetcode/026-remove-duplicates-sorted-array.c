int removeDuplicates(int *nums, int numsSize) {
  int prior = nums[0] - 1;
  int i = 0; // trailing pointer
  int j = 0; // leading pointer
  while (j < numsSize) {
    if (nums[j] != prior)
      nums[i++] = nums[j];
    prior = nums[j++];
  }
  return i;
}
