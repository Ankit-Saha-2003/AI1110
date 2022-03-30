/*
ICSE 2019 Grade 10
Question 1(b)

Name: Ankit Saha
Roll number: AI21BTECH11004

Problem Statement
A man invests Rs 4500 in shares of a company which is paying 7.5% dividend. If Rs 100 shares are available at a discount of 10%, find:
(i) the number of shares he purchases
(ii) his annual income
*/

#include <stdio.h>

// Function prototypes
int numberOfShares(double investment, double faceValue, double discount);
double annualIncome(double investment, double dividend, double discount);

int main() {
    double P = 4500.0;    // Total investment made by the man
    double F = 100.0;     // Face value of a share
    double d = 10.0;      // Discount at which the shares are available
    double D = 7.5;       // Dividend

    // Output
    printf("The man purchased %d shares\n", numberOfShares(P, F, d));
    printf("The annual income of the man is Rs %.2lf\n", annualIncome(P, D, d));
}

// Returns the number of shares purchased
int numberOfShares(double investment, double faceValue, double discount) {
    int N = (100 * investment) / (faceValue * (100 - discount));
    return N;
}

// Returns the annual income earned
double annualIncome(double investment, double dividend, double discount) {
    double A = (investment * dividend) / (100 - discount);
    return A;
}