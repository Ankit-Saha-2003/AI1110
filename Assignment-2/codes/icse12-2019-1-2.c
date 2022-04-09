/*
ICSE 2019 Grade 12
Question 1(ii)

Name: Ankit Saha
Roll number: AI21BTECH11004

Problem Statement
Solve: sin(2arctan(x)) = 1
*/

#include <stdio.h>
#include <math.h>

// Function prototypes
float f(float x);
void writeCoords();

int main() {
    float x = 1.0;
    if (f(x) == 1.0) {
        printf("x = %g is a solution\n", x);
    } else {
        printf("x = %g is not a solution\n", x);
    }
    writeCoords();
}

// Returns the value of the given function at x
float f(float x) {
    return sin(2 * atan(x));
}

// Writes the x and y coordinates into a .dat file
void writeCoords() {
    FILE *fp = fopen("points.dat", "w");
    if (!fp) {
        printf("Couldn't open file\n");
        return;
    }
    for (float i = -6; i <= 6; i += 0.01) {
        fprintf(fp, "%f %f\n", i, f(i));
    }
    fclose(fp);
    return;
}