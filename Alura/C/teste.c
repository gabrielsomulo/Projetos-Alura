#include <stdio.h>

int numSecreto = 1;
int chute;

int main(){
    //Comentário
    printf("********************\n Ola Mundo\n********************\n");

    printf("Qual o numero ?\n");
    scanf("%d", &chute);
    printf("Numero do chute e: %d", chute);

    if (numSecreto == chute){
        printf("\nParabens voce acertou !!!");
    }
    else if(numSecreto < chute){
        printf("\nSeu numero e maior que o numero secreto !!!");
    }
    else{
        printf("\nSeu numero e menor que o numero secreto !!!");
    }
}
