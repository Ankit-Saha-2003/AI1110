// Calculates the mean and variance of a uniform distribution

// Name: Ankit Saha
// Roll number: AI21BTECH11004

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "header.h"

#define NUM 1000000

int main() {
	double *data = readData("uni.dat", 1000000);
	
	printf("Empirical Mean = %lf\n", mean(data, 1000000));
	printf("Theoretical Mean = %lf\n", 1.0/2);

	printf("Empirical Variance = %lf\n", variance(data, 1000000));
	printf("Theoretical Variance = %lf\n", 1.0/12);

	return 0;
}
