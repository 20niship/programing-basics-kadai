#include <math.h>
#include <stdio.h>


int mod_apm(int a, int p, int m){
  if(p == 0) return 1;
  if(p == 1) return a % m;
  return (a * mod_apm(a, p - 1, m)) % m;
}

int main(){
  int answer = mod_apm(541, 1234, 1299709);
  printf("%d\n", answer);
  return 0;
}
