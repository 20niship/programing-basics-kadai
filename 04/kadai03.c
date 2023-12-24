#include <stdio.h>
#include <string.h>

void reverse(char* s);
int main() {
  char s[] = "hello";
  reverse(s);
  printf("%s\n", s); // 出力は"olleh"
  return 0;
}

void reverse(char* s) {
  int l = strlen(s);
  char tmp[l + 1];
  strcpy(tmp, s);

  for(int i = 0; i < l; i++) 
    s[i] = tmp[l - i - 1];
}
