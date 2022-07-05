// Writes to a file the probabilities P_{e|0} and P_{e|1} for different values of A

// Name: Ankit Saha
// Roll number: AI21BTECH11004

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "header.h"

#define NUM 1000000

int main() {
	FILE *fp = fopen("5.7.dat", "w");
	for (double A = 0; A <= 10; A += 0.25) {
		int e_0 = 0;
		int e_1 = 0;
		generateY("y.dat", NUM, A);
		double *y_data = readData("y.dat", NUM);
		double *x_data = readData("x.dat", NUM);
		for (int i = 0; i < NUM; i++) {
			if (y_data[i] < 0 && x_data[i] > 0) {
				e_0++;
			} else if (y_data[i] > 0 && x_data[i] < 0) {
				e_1++;
			}
		}	
		double p_e_0 = (double)e_0 / NUM;
		double p_e_1 = (double)e_1 / NUM;
		fprintf(fp, "%lf %lf\n", p_e_0, p_e_1);
	}
	fclose(fp);
	return 0;	
}
