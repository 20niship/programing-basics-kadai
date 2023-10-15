#include <math.h>
#include <stdio.h>

#define PRIME_LIST_SIZE 10000
int prime_list[PRIME_LIST_SIZE];
int prime_list_size = 0;

void calc_primes(int max_) {
  for(int i = 2; i <= max_; i++) {
    for(int j = 0; j < prime_list_size; j++)
      if(i % prime_list[j] == 0) goto CONTINUE_NEXT;

    printf("%d is prime\n", i);
    prime_list[prime_list_size] = i;
    prime_list_size++;

  CONTINUE_NEXT : {}
  }
}

double get_pi() {
  double mul = 1.0;
  for(int i = 0; i < prime_list_size; i++) {
    mul *= 1.0 - 1.0 / pow(prime_list[i], 2);
  }
  return sqrt(6. / mul);
}

int main() {
  calc_primes(10000);
  for(int i = 0; i < prime_list_size; i++) {
    printf("%d\n", prime_list[i]);
  }
  double pi = get_pi();
  printf("pi = %f\n", pi);
  return 0;
}
