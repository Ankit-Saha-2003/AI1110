// Generates 1000000 samples of a Gaussian random variable taking values between -6 and 6 and stores them in a file called uni.dat

// Name: Ankit Saha
// Roll number: AI21BTECH11004

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define NUM 1000000

int main() {
	FILE *fp = fopen("gau.dat", "w");
	if (!fp) {
		printf("Couldn't open file\n");
		return 1;
	}

	for (int i = 0; i < NUM; i++) {
		double sum = -6.0;
		for (int j = 0; j < 12; j++) {
			sum += (double)rand()/RAND_MAX;
		}	
		fprintf(fp, "%lf\n", sum);
	}
	fclose(fp);
	return 0;	
}
