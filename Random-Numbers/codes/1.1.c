// Generates 1000000 samples of a uniform random variable taking values between 0 and 1 and stores them in a file called uni.dat

// Name: Ankit Saha
// Roll number: AI21BTECH11004

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "header.h"

#define NUM 1000000

int main() {
	generateUniform("uni.dat", 1000000);
	return 0;	
}
