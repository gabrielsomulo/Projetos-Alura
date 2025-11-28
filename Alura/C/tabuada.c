#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int val, res, e_valido;

int main(){
    while(!e_valido){
        printf("Tabuada \n");
        printf("Insira o valor para calcular: \n");
        scanf("%d", &val);

        e_valido = (val>0);

        if(e_valido){
            for(int i=1; i<=10; i++){
                res = val*i;
                printf("%d X %d = %d \n", val, i, res);
            }
        }else{
            printf("Insira um valor maior que zero \n");
        }
    }
}