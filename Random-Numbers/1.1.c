// Generates 1000000 samples of a uniform random variable taking values between 0 and 1 and stores them in a file called uni.dat

// Name: Ankit Saha
// Roll number: AI21BTECH11004

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
	FILE *fp = fopen("uni.dat", "w");
	int NUM = 1000000;
	for (int i = 0; i < NUM; i++) {
		fprintf(fp, "%lf\n", (double)rand()/RAND_MAX);
	}
	fclose(fp);	
}
