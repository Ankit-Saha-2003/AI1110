// Writes to a file the probabilities P_e for different values of A

// Name: Ankit Saha
// Roll number: AI21BTECH11004

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "header.h"

#define NUM 1000000

int main() {
	FILE *fp = fopen("8.3.dat", "w");
	for (double snr = 0; snr <= 10; snr += 0.25) {
		int e = 0;
		int total = 0;
		generateY_2D("8.3.y.dat", NUM, sqrt(snr));
		double **y_data = readMatrix("8.3.y.dat", NUM, 2);
		double **x_data = readMatrix("ber2d.dat", NUM, 2);
		for (int i = 0; i < NUM; i++) {
			if (y_data[i][1] - y_data[i][0] > 0 && x_data[i][0] > 0.5) {
				e++;
			} 
			if (x_data[i][0] > 0.5) {
				total++;
			}
		}	
		double p_e = (double)e / total;
		fprintf(fp, "%lf\n", p_e);
		free(y_data);
		free(x_data);
	}
	fclose(fp);
	return 0;	
}
