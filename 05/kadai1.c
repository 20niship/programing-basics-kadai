#include <math.h>
#include <stdio.h>


#define MAX_LEN 100

const char* fname = "./namelist.txt";

int main() {
  char buffer[MAX_LEN];
  FILE* fp;
  fp = fopen(fname, "r");
  if(fp == NULL) {
    printf("Failed to open the file\n");
    return 1;
  }


  int sum_age = 0;
  float sum_height = 0;
  float sum_weight = 0;

  float sum_age2 = 0;
  float sum_height2 = 0;
  float sum_weight2 = 0;

  int min_age = 1000;
  int max_age = 0;

  float min_height = 1000;
  float max_height = 0;

  float min_weight = 1000;
  float max_weight = 0;

  int count = 0;

  while(fgets(buffer, MAX_LEN, fp) != NULL) {
    char name[MAX_LEN];
    int age;
    float height;
    float weight;
    sscanf(buffer, "%[^,],%d,%f,%f\n", name, &age, &height, &weight);
    sum_age += age;
    sum_height += height;
    sum_weight += weight;
    sum_age2 += age * age;
    sum_height2 += height * height;
    sum_weight2 += weight * weight;
    min_age = age < min_age ? age : min_age;
    max_age = age > max_age ? age : max_age;
    min_height = height < min_height ? height : min_height;
    max_height = height > max_height ? height : max_height;
    min_weight = weight < min_weight ? weight : min_weight;
    max_weight = weight > max_weight ? weight : max_weight;


    count++;
  }

  float ave_age = (float)sum_age / count;
  float ave_height = sum_height / count;
  float ave_weight = sum_weight / count;

  float stdev_age = sqrt((float)sum_age2 / count - (float)sum_age * sum_age / count / count);
  float stdev_height = sqrt(sum_height2 / count - sum_height * sum_height / count / count);
  float stdev_weight = sqrt(sum_weight2 / count - sum_weight * sum_weight / count / count);


  printf("Age : (max,min,mean,stdev) = (%d, %d, %f, %f)\n", max_age, min_age, ave_age, stdev_age);
  printf("Height : (max,min,mean,stdev) = (%f, %f, %f, %f)\n", max_height, min_height, ave_height, stdev_height);
  printf("Weight : (max,min,mean,stdev) = (%f, %f, %f, %f)\n", max_weight, min_weight, ave_weight, stdev_weight);

  fclose(fp);
  return 0;
}
