// Generates 1000000 samples of a Gaussian random variable taking values between -6 and 6 and stores them in a file called uni.dat

// Name: Ankit Saha
// Roll number: AI21BTECH11004

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "header.h"

#define NUM 1000000

int main() {
	generateGaussian("gau.dat", 1000000, 12);
	return 0;	
}
