// Generates 1000000 samples of a uniform random variable taking values between 0 and 1 and stores them in a file called uni.dat

// Name: Ankit Saha
// Roll number: AI21BTECH11004

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define NUM 1000000

int main() {
	FILE *fp = fopen("uni.dat", "w");
	if (!fp) {
		printf("Couldn't open file\n");
		return 1;
	}

	for (int i = 0; i < NUM; i++) {
		fprintf(fp, "%lf\n", (double)rand()/RAND_MAX);
	}
	fclose(fp);
	return 0;	
}
