#include <stdio.h>

int sharedVar = 42;  // Definition of extern variable

void printVar();

int main() {
    printVar();  // Call function from file1.c
    printf("Value of sharedVar from file2.c: %d\n", sharedVar);
    return 0;
}
