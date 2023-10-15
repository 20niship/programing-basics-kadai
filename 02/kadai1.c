#include <math.h>
#include <stdio.h>

double calc_pi(int max_iter) {
  double sum = 0.0;
  for(int i = 1; i < max_iter; i++) {
    sum += 1.0 / (pow(i, 2) * pow(2, i - 1));
  }
  sum += pow(log(2), 2);
  return sqrt(6 * sum);
}

int main() {
  double pi = calc_pi(100000000);
  printf("pi = %f\n", pi);
  return 0;
}
