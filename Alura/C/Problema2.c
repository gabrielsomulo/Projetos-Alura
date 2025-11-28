#include <stdio.h>

int i = 1;
int resultado;

int main(){
    //for (int i =1; i<=100; i++){
    //   printf("%d\n", i);
    //}

    while (i<=100){
        printf("%d\n", i);
        resultado += i;
        i++;
    }
    printf("%d", resultado);

}