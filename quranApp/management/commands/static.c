#include <stdio.h>

void staticVarExample() {
    static int count = 0;  // Static variable
    count++;
    printf("Static Variable Count: %d\n", count);
}

int main() {
    for(int i=0;i<3;i++){
    staticVarExample();  // Call first time
    staticVarExample();  // Call second time
    }
    return 0;
}
