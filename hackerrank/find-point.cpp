#include <iostream>
using namespace std;

int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    int px, py, qx, qy;
    cin >> px >> py >> qx >> qy;
    cout << qx + qx - px << ' ' << qy + qy - py << endl;
  }
  return 0;
}
