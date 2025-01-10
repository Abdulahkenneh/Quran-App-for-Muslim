#include <stdio.h>

extern int sharedVar;  // Declaration of extern variable

void printVar() {
    printf("Value of sharedVar from file1.c: %d\n", sharedVar);
}
