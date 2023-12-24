#include <assert.h>
#include <stdio.h>
#include <string.h>

int roman2num(char*);
int main() {
  // Examples
  printf("XIV = %d\n", roman2num("XIV"));             // 14
  printf("CDXCV = %d\n", roman2num("CDXCV"));         // 495
  printf("MCMXLV = %d\n", roman2num("MCMXLV"));       // 1945
  printf("MMMCMXCIX = %d\n", roman2num("MMMCMXCIX")); // 3999
  return 0;
}

int s2v(char s) {
  switch(s) {
    case 'I': return 1;
    case 'V': return 5;
    case 'X': return 10;
    case 'L': return 50;
    case 'C': return 100;
    case 'D': return 500;
    case 'M': return 1000;
    default: assert("ERROR"); return 0;
  }
}

int roman2num(char* s) {
  int size = strlen(s);
  int sum = 0;

  int i = 0;
  while(i < size) {
    int v = s2v(s[i]);
    if(i + 1 < size  && s2v(s[i + 1]) > v) {
      sum += s2v(s[i + 1]) - v;
      i += 2;
    } else {
      sum += v;
      i++;
    }
  }
  return sum;
}
