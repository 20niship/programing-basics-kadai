#include <assert.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>


// x*x+ y*y = z*z のとき、x < zかつy<zである.
// 重複をなくすためにx <= yという制約を加えると
// ピタゴラス数となったa/bのリストを記録して、新しく見つけたa2, b2に対してa2 / b2が過去のいずれかの値と一致したら互いに素ではない

// x<1000, y<1000, z<1000の場合を考える

#define AB_LIST_SIZE 1000000
double ab_list[AB_LIST_SIZE];
size_t ab_list_size = 0;

// 互いに素なものがすでに存在するか
bool has_coprime(int a, int b) {
  for(int i = 0; i < ab_list_size; i++) {
    double diff = ab_list[i] - (double)a / (double)b;
    if(diff < 1e-10) return false;
  }
  return true;
}

void push_back_ab_list(int a, int b) {
  assert(has_coprime(a, b));
  assert(ab_list_size < AB_LIST_SIZE);
  ab_list[ab_list_size] = (double)a / (double)b;
  ab_list_size++;
}

// ピタゴラス数を計算
void print_pythagoras() {
  for(int x = 1; x < 1000; x++) {
    for(int y = x + 1; y < 1000; y++) {
      int z = sqrt(x * x + y * y);
      if(z >= 1000) continue;
      // ピタゴラス数かどうか
      if(!(x * x + y * y == z * z)) continue;
      // 互いに素かどうか
      if(!has_coprime(x, y)) continue;
      push_back_ab_list(x, y);
      printf("%d^2 + %d^2 = %d^2\n", x, y, z);
    }
  }
}

int main() {
  print_pythagoras();
  return 0;
}
