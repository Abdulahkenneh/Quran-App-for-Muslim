#include <stdio.h>

int main(void) {
    int row = 2, col = 3;
    int firstarr[row][col], secondarr[row][col], sumarr[row][col];

    // Input: Enter the elements of the first matrix
    printf("Enter the elements of the first 2 x 3 matrix:\n");
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            scanf("%d", &firstarr[i][j]);
        }
    }

    // Print the first matrix
    printf("First Matrix:\n");
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            printf("%d ", firstarr[i][j]);
        }
        printf("\n");
    }

    // Input: Enter the elements of the second matrix
    printf("Enter the elements of the second 2 x 3 matrix:\n");
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            scanf("%d", &secondarr[i][j]);
        }
    }

    // Print the second matrix
    printf("Second Matrix:\n");
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            printf("%d ", secondarr[i][j]);
        }
        printf("\n");
    }

    // Calculate the sum of the two matrices
    printf("The sum of the two matrices is:\n");
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            sumarr[i][j] = firstarr[i][j] + secondarr[i][j]; // Calculate sum
            printf("%d ", sumarr[i][j]); // Print sum
        }
        printf("\n"); // New line for next row
    }

    return 0;
}
