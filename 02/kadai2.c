#include <math.h>
#include <stdio.h>


int get_date(size_t y, size_t m, size_t d) {}
#include <math.h>
#include <stdio.h>

int zeller(int, int, int);

int main() {
  int year = 2016, month = 10, day = 5;
  int w;
  w = zeller(year, month, day);
  printf("%d/%d/%d is ", month, day, year);
  switch(w) {
    case 0: printf("Sat.\n"); break;
    case 1: printf("Sun.\n"); break;
    case 2: printf("Mon.\n"); break;
    case 3: printf("Tue.\n"); break;
    case 4: printf("Wed.\n"); break;
    case 5: printf("Thurs.\n"); break;
    case 6: printf("Fri.\n"); break;
  }
  return 0;
}
int zeller(int year, int month, int day) { /*この関数を埋める*/
  int w = year + floor((float)year / 4) - floor((float)year / 100) + floor((float)year / 400) + floor((float)(13 * month + 8) / 5) + day;
  return w % 7;
}
