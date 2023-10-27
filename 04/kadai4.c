#include <stdio.h>
#include <string.h>

void uppercase(char* s);

int main() {
  char s[] = "hello world";
  uppercase(s);
  printf("%s\n", s); // 出力は"HELLO WORLD"
  return 0;
}

void uppercase(char* s) {
  const int gap = 'A' - 'a';
  int size = strlen(s);
  for(int i = 0; i < size; i++) {
    if(s[i] >= 'a' && s[i] <= 'z') s[i] += gap;
  }
}
