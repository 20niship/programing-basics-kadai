#include <math.h>
#include <stdio.h>

int main() {
  int n = 158340421;
  for(int i = 0; i < sqrt(n); i++) {
    if(pow(i, 3) == n) {
      printf("%d**3 = %d\n", i, n);
      break;
    }
  }
  return 0;
}
