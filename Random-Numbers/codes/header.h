#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function prototypes
double *readData(char *file, int size);
double mean(double *data, int num);
double variance(double *data, int num);

// Reads data from file into array and returns the array
double *readData(char *file, int size) {
	double *data = (double *)malloc(size * sizeof(double));
	FILE *fp = fopen(file, "r");
	if (!fp) {
		printf("Couldn't open file\n");
		return NULL;
	}
	for (int i = 0; i < size; i++) {
		fscanf(fp, "%lf", &data[i]);
	}
	return data;
}

// Returns the mean of data
double mean(double *data, int num) {
	double sum = 0;
	for (int i = 0; i < num; i++) {
		sum += data[i];
	}
	return sum / num;
}

// Returns the variance of data
double variance(double *data, int num) {
	double varsum = 0;
	double mu = mean(data, num);
	for (int i = 0; i < num; i++) {
		varsum += pow(data[i] - mu, 2);
	}
	return varsum / num;
}
