#include <stdio.h>

#define PRIME 1
#define NOT_PRIME 0

int is_prime(int); /*引数が素数の場合 1，それ以外の場合 0を返す*/

int main() {
  int i;
  for(i = 2; i <= 1000; i++) {
    if(is_prime(i) == 1) {
      printf("%d is prime\n", i);
    }
  }
}

int is_prime(int n) {
  int i;
  for(i = 2; i < n; i++)
    if(n % i == 0) return NOT_PRIME;
  return PRIME;
}
