// Writes to a file the probabilities P_e for different values of gamma

// Name: Ankit Saha
// Roll number: AI21BTECH11004

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "header.h"

#define NUM 1000000

int main() {
	FILE *fp = fopen("7.1.dat", "w");
	for (double gamma = 0; gamma <= 10; gamma += 0.25) {
		int e = 0;
		int total = 0;
		double sigma = sqrt(gamma/2);
		generateY_Rayleigh("7.1.y.dat", NUM, sigma);
		double *y_data = readData("7.1.y.dat", NUM);
		double *x_data = readData("7.1.x.dat", NUM);
		for (int i = 0; i < NUM; i++) {
			if (y_data[i] < 0 && x_data[i] > 0) {
				e++;
			}
			if (x_data[i] > 0) {
				total++;
			}
		}	
		double p_e = (double)e / total;
		fprintf(fp, "%lf\n", p_e);
	}
	fclose(fp);
	return 0;	
}
