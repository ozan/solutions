#include <assert.h>

int canCompleteCircuit(int *gas, int gasSize, int *cost, int costSize) {
  for (int i = 0; i < gasSize; i++) {
    int fail = 0, tank = 0;

    for (int delta = 0; delta < gasSize; delta++) {
      tank += gas[(i + delta) % gasSize] - cost[(i + delta) % gasSize];
      if (tank < 0) {
        fail = 1;
        break;
      }
    }

    if (!fail)
      return i;
  }
  return -1;
}

int main() {
  int gas_0[] = {10, 20, 30};
  int cost_0[] = {9, 19, 29};
  int gas_1[] = {9, 20, 30};
  int cost_1[] = {10, 19, 29};
  int gas_fail[] = {10, 20, 30};
  int cost_fail[] = {11, 21, 31};

  assert(canCompleteCircuit(gas_0, 3, cost_0, 3) == 0);
  assert(canCompleteCircuit(gas_1, 3, cost_1, 3) == 1);
  assert(canCompleteCircuit(gas_fail, 3, cost_fail, 3) == -1);
  return 0;
}
