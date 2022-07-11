#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function prototypes
double *readData(char *file, int size);
double **readMatrix(char *file, int rows, int cols);
double mean(double *data, int num);
double variance(double *data, int num);
void generateUniform(char *file, int count);
void generateGaussian(char *file, int count, int num);
double randomUniform();
double randomGaussian(int num);
int randomBernoulli();
void generateY(char *file, int count, double A);
double chiSquared(int deg, double sigma);
double randomRayleigh(double sigma);
void generateY_Rayleigh(char *file, int count, double sigma);
void generate2DBernoulli(char *file, int count);
void generate2DGaussian(char *file, int count);
void generateY_2D(char *file, int count, double A);

// Reads data from file into array and returns the array
double *readData(char *file, int size) {
	double *data = (double *)malloc(size * sizeof(double));
	FILE *fp = fopen(file, "r");
	if (!fp) {
		printf("Couldn't open file\n");
		return NULL;
	}
	for (int i = 0; i < size; i++) {
		fscanf(fp, "%lf", &data[i]);
	}
	fclose(fp);
	return data;
}

// Reads matrix from file into 2D array and returns the array
double **readMatrix(char *file, int rows, int cols) {
	double **matrix = (double **)malloc(rows * sizeof(double *));
	for (int i = 0; i < rows; i++) {
		matrix[i] = (double *)malloc(cols * sizeof(double));
	}
	FILE *fp = fopen(file, "r");
	if (!fp) {
		printf("Couldn't open file\n");
		return NULL;
	}
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			fscanf(fp, "%lf", &matrix[i][j]);
		}
	}
	fclose(fp);
	return matrix;
}

// Returns the mean of data
double mean(double *data, int num) {
	double sum = 0;
	for (int i = 0; i < num; i++) {
		sum += data[i];
	}
	return sum / num;
}

// Returns the variance of data
double variance(double *data, int num) {
	double varsum = 0;
	double mu = mean(data, num);
	for (int i = 0; i < num; i++) {
		varsum += pow(data[i] - mu, 2);
	}
	return varsum / num;
}

// Generates count number of samples of a uniform random variable taking values between 0 and 1 and stores them in a file
void generateUniform(char *file, int count) {
	FILE *fp = fopen(file, "w");
	if (!fp) {
		printf("Couldn't open file\n");
		return;
	}
	for (int i = 0; i < count; i++) {
		fprintf(fp, "%lf\n", (double)rand()/RAND_MAX);
	}
	fclose(fp);
	return;
}

// Generates count number of samples of a Gaussian random variable taking values between -num/2 and num/2 and stores them in a file
void generateGaussian(char *file, int count, int num) {
	FILE *fp = fopen(file, "w");
        if (!fp) {
                printf("Couldn't open file\n");
                return;
        }
        for (int i = 0; i < count; i++) {
                double sum = num/(-2.0);
                for (int j = 0; j < num; j++) {
                        sum += (double)rand()/RAND_MAX;
                }
                fprintf(fp, "%lf\n", sum);
        }
        fclose(fp);
	return;
}

// Returns a random uniformly distributed value 
double randomUniform() {
	return (double)rand()/RAND_MAX;
}

// Returns a random normally distributed value
double randomGaussian(int num) {
	double sum = num/(-2.0);
        for (int j = 0; j < num; j++) {
        	sum += randomUniform();
        }
	return sum;
}

// Returns a random Bernoulli distributed value in {-1,1}
int randomBernoulli() {
	return 2*(rand()%2) - 1;
}

// Generates count samples of a random variable Y = AX + N
void generateY(char *file, int count, double A) {
	FILE *y_file = fopen(file, "w");
	if (!y_file) {
		printf("Couldn't open file\n");
		return;
	}
	FILE *x_file = fopen("x.dat", "w");
	if (!x_file) {
		printf("Couldn't open file\n");
		return;
	}	
        for (int i = 0; i < count; i++) {
		int X = randomBernoulli();
		double N = randomGaussian(12);
                double Y = A * X + N;
                fprintf(y_file, "%lf\n", Y);
		fprintf(x_file, "%d\n", X);
        }
        fclose(y_file);
	fclose(x_file);
	return;
}

double chiSquared(int deg, double sigma) {
	double sum = 0;
	for (int i = 0; i < deg; i++) {
		double X = sigma * randomGaussian(12);
		sum += pow(X, 2);
	}
	return sum;
}

double randomRayleigh(double sigma) {
        return sqrt(chiSquared(2, sigma));
}

void generateY_Rayleigh(char *file, int count, double sigma) {
	FILE *y_file = fopen(file, "w");
	if (!y_file) {
		printf("Couldn't open file\n");
		return;
	}
	FILE *x_file = fopen("7.1.x.dat", "w");
	if (!x_file) {
		printf("Couldn't open file\n");
		return;
	}	
        for (int i = 0; i < count; i++) {
		int X = randomBernoulli();
		double N = randomGaussian(12);
		double A = randomRayleigh(sigma);
                double Y = A * X + N;
                fprintf(y_file, "%lf\n", Y);
		fprintf(x_file, "%d\n", X);
        }
        fclose(y_file);
	fclose(x_file);
	return;
}

void generate2DBernoulli(char *file, int count) {
	FILE *fp = fopen(file, "w");
        if (!fp) {
                printf("Couldn't open file\n");
                return;
        }
        for (int i = 0; i < count; i++) {
                int x = randomBernoulli();
		if (x == 1) fprintf(fp, "1 0\n");
		else fprintf(fp, "0 1\n");
        }
        fclose(fp);
	return;	
}

void generate2DGaussian(char *file, int count) {
	FILE *fp = fopen(file, "w");
        if (!fp) {
                printf("Couldn't open file\n");
                return;
        }
        for (int i = 0; i < count; i++) {
        	double N1 = randomGaussian(12);
		double N2 = randomGaussian(12);
		fprintf(fp, "%lf %lf\n", N1, N2);
	}
        fclose(fp);
	return;	
}
void generateY_2D(char *file, int count, double A) {
	FILE *fp = fopen(file, "w");
        if (!fp) {
                printf("Couldn't open file\n");
                return;
        }
	generate2DBernoulli("ber2d.dat", count);	
	generate2DGaussian("gau2d.dat", count);
	double **X = readMatrix("ber2d.dat", count, 2);
	double **N = readMatrix("gau2d.dat", count, 2);
	for (int i = 0; i < count; i++) {
		double y1 = A * X[i][0] + N[i][0];
		double y2 = A * X[i][1] + N[i][1];
		fprintf(fp, "%lf %lf\n", y1, y2);
	}
	fclose(fp);
	free(X);
	free(N);
	return;
}
