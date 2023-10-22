#include <assert.h>
#include <math.h>
#include <stdio.h>

double P(int n, double x) {
  if(n == 0) return 1;
  if(n == 1) return x;
  return ((2 * n - 1) * x * P(n - 1, x) - (n - 1) * P(n - 2, x)) / n;
}

int main() {
  double a = P(16, 0.5);
  assert(fabs(a + 0.1498) < 0.001);
  printf("P(16, 0.5) = %f\n", a); // P(16, 0.5) = -0.1498 (正解

  double b = P(32, 0.7);
  assert(fabs(b - 0.1651) < 0.001);
  printf("P(32, 0.7) = %f\n", b); // P(32, 0.7) = 0.1651 (正解

  /* double c = P(128, 0.5); */
  /* printf("P(128, 0.5) = %f\n", c); */
  // 学習が終わらない理由：
  // 　上のように愚直に実装した場合
  // 　Pn(x) (n > 1)に対して、再帰呼出しの回数は2**(n-1)回となるので、nの数が大きくなると計算量が爆発的に増える
  // しかし、xの値は再帰の間で変わらないので、メモ化を行うことでn-1回の再帰に計算量を削減できる
}
