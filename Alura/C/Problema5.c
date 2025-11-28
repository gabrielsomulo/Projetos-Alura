#include <stdio.h>

int total;

int num[10];


int soma(int*num, int a){
    for (int i = 0; i < a; i++)
    {
        total += num[i];
    }

    return total;
}

int main(){
    num[0] = 2;
    num[1] = 5;
    num[2] = 3;
    num[3] = 7;
    num[4] = 8;
    num[5] = 9;
    num[6] = 5;
    num[7] = 3;
    num[8] = 2;
    num[9] = 1;
    
    int resposta = soma(&num, 10);
    printf("Resposta: %d \n\n", resposta);
}