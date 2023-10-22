#include <assert.h>
#include <math.h>
#include <stdio.h>

const float EPS = 1e-6;

double f(double);

double dfdx(double);

double newton(double);

int main() {
  double x0 = 1.0;
  double solution = newton(x0);
  printf("solution is %f\n", solution);

  assert(fabs(solution - (-0.567143)) < 0.001);
  return 0;
}

double f(double x) {
  return exp(x) + x;
}

double dfdx(double x) {
  return exp(x) + 1;
}


double newton(double x) {
  if(fabs(f(x)) < EPS) return x;
  double new_x = x - f(x) / dfdx(x);
  return newton(new_x);
}
