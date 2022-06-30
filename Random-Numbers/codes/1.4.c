// Calculates the mean and variance of a uniform distribution

// Name: Ankit Saha
// Roll number: AI21BTECH11004

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define NUM 1000000

int main() {
	double data[NUM];
	FILE *fp = fopen("uni.dat", "r");
	if (!fp) {
		printf("Couldn't open file\n");
		return 1;
	}
	double sum = 0;
	for (int i = 0; i < NUM; i++) {
		fscanf(fp, "%lf", &data[i]);
		sum += data[i];
	}
	double mean = sum/NUM;
	printf("Empirical Mean = %lf\n", mean);
	printf("Theoretical Mean = %lf\n", 1.0/2);

	double varsum = 0;
	for (int i = 0; i < NUM; i++) {
		varsum += pow(data[i] - mean, 2);
	}
	double variance = varsum/NUM;
	printf("Empirical Variance = %lf\n", variance);
	printf("Theoretical Variance = %lf\n", 1.0/12);

	return 0;
}
