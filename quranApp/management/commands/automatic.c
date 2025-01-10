#include <stdio.h>
int automaticVar = 0; 
void automaticVarExample() {
     // Automatic variable
    automaticVar++;
    printf("Automatic Variable Value: %d\n", automaticVar);
   
}

int main() {
    for(int i=0;i<3;i++){
    automaticVarExample();  // Call first time
    automaticVarExample();  // Call second time
    }
    return 0;

}
