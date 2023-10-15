#include <assert.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

void print_pythagoras() {
  for(int x = 1; x < 1000; x++) {
    for(int y = x + 1; y < 1000; y++) {
      int z = sqrt(x * x + y * y);
      if(z >= 1000) continue;
      // ピタゴラス数かどうか
      if(!(x * x + y * y == z * z)) continue;
      // 互いに素かどうか
      printf("%d^2 + %d^2 = %d^2\n", x, y, z);
    }
  }
}

int main() {
  print_pythagoras();
  return 0;
}
