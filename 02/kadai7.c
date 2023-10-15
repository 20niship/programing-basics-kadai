#include <assert.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>

// ゴールドバッハ予想の結果を格納する配列
// i番目には, i*2 = sum_list[i][0] + sum_list[i][1]となる素数の組が格納される
unsigned short sum_list[500][2];

void clear() {
  for(int i = 0; i < 500; i++) {
    sum_list[i][0] = 0;
    sum_list[i][1] = 0;
  }
}

// 1000以下の素数を列挙
int primes[1000];
int primes_size = 0;
void get_primes() {
  primes_size = 0;
  for(int i = 2; i < 1000; i++) {
    for(int j = 0; j < primes_size; j++)
      if(i % primes[j] == 0) goto CONTINUE_NEXT;
    primes[primes_size] = i;
    primes_size++;
  CONTINUE_NEXT : {}
  }
}

void calc_goldbach() {
  for(int i = 0; i < primes_size; i++) {
    for(int j = 0; j < primes_size; j++) {
      int sum = primes[i] + primes[j];
      if(sum > 1000 || sum % 2 == 1) continue;
      // if(sum_list[sum / 2][0] != 0) continue;
      sum_list[sum / 2][0] = primes[i];
      sum_list[sum / 2][1] = primes[j];
    }
  }
}

void print_goldbach() {
  for(int i = 2; i < 500; i++) {
    printf("%d  = %d + %d\n", i * 2, sum_list[i][0], sum_list[i][1]);
  }
}

// 足し算があっていることを確認
void check_result() {
  for(int i = 2; i < 500; i++) {
    assert(sum_list[i][0] + sum_list[i][1] == i * 2);
  }
}

int main() {
  clear();
  get_primes();
  calc_goldbach();
  print_goldbach();
  check_result();
  return 0;
}
