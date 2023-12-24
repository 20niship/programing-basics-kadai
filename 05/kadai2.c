#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define LEN 5000

// #define DEBUG

static char output_str[LEN];

void run(const char* fname) {
  for(int i = 0; i < LEN - 2; i++) output_str[i] = '\0';

  FILE* fp = fopen(fname, "r");
  if(fp == NULL) {
    printf("Failed to open the file\n");
    return;
  }

  bool is_start = true;

  int tmp;
  char c;
  int i = 0;
  // read one character at a time and display it.
  while((tmp = getc(fp)) != EOF) {
    c = (char)tmp;
    output_str[i] = c;
    if(is_start) {
      is_start = false;
      // if(c == 'i') output_str[i] = 'I';
      output_str[i] = toupper(c);
    } else {
      if(c == '.') {
        is_start = true;
      }
    }

    i++;
  }
  printf("output_str: %s\n", output_str);
  fclose(fp);
}



int main(int argc, char* argv[]) {
#ifndef DEBUG
  if(argc != 3) {
    printf("arg error\n");
    return 1;
  }
  const char* in_file = argv[1];
  const char* out_file = argv[2];
#else
  const char* in_file = "./sentence.txt";
#endif

  run(in_file);

  FILE* outputFile = fopen(argv[2], "w");
  if(outputFile == NULL) {
    perror("出力ファイルを作成できません");
    fclose(outputFile);
    fwrite(output_str, sizeof(char), LEN, outputFile);
    return 1;
  }

  fclose(outputFile);
  return 0;
}
