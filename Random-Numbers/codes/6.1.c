// Generates 1000000 samples of a chi-squared random variable with 2 degrees of freedom and stores them in a file called chi.dat

// Name: Ankit Saha
// Roll number: AI21BTECH11004

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "header.h"

#define NUM 1000000

int main() {
	FILE *fp = fopen("chi.dat", "w");
	if (!fp) {
		printf("Couldn't open file\n");
		return 1;
	}
	for (int i = 0; i < NUM; i++) {
		double X1 = randomGaussian(12);
		double X2 = randomGaussian(12);
		fprintf(fp, "%lf\n", X1*X1 + X2*X2);
	}
	fclose(fp);
	return 0;	
}
