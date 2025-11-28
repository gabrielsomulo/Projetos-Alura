#include <stdio.h>

int x,y,resultado;

int main(){

    printf("Multiplicadora: \n");
    printf("X - ");
    scanf("%d", &x);
    printf("Y - ");
    scanf("%d", &y);

    resultado = x*y;

    printf("%d x %d = %d \n", x,y,resultado);
}