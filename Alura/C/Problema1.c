
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//#define VZS 5


int acertou, chute, numerosecreto, numerogrande, segundos,vzs, tentativas, nivel;
double pontos = 1000;
double pontosPdds;


int main(){

    segundos = time(0);
    srand(segundos);
    numerogrande = rand();

    numerosecreto = numerogrande % 100;

    printf("********************\n Ola Mundo\n********************\n");

    while (!acertou)
    {
        vzs = 0;    

        printf("Escolha o nível de dificuldade:\n\n 1-Fácil   2- Médio    3- Difícil\n\n");
        printf("Escolha: ");
        scanf("%d", &nivel);

        /*if(nivel == 1){
            cc
        }else if(nivel == 2){
            tentativas = 10;
        }else if (nivel == 3){
            tentativas = 5;
        }else{
            printf("\nValor incorreto !!!\n");
            tentativas = 5;
        }*/

        switch (nivel)
        {
        case 1:
            tentativas = 20;
            break;

        case 2:
            tentativas = 10;
            break;

        default:
            tentativas = 5;
            break;
        }
        

        for(int i= 1; i<=tentativas; i++){
            vzs++;
            printf("\nTentativa %d\n", vzs);
            printf("Qual o numero ?\n");
            scanf("%d", &chute);
            printf("Numero do chute e: %d\n", chute);

            if (chute<0){
                printf("Não pode númeors menores que 0\n");
                continue;
            }

            acertou = (chute == numerosecreto);

            if(acertou) {
                break;
            } 
            else if (chute > numerosecreto){
                printf("Seu chute foi maior do que o número secreto!\n");
            } 
            else{
                printf("Seu chute foi menor do que o número secreto!\n");
            
            }
            
            pontosPdds = (chute-numerosecreto)/2;
            pontosPdds = abs(pontosPdds);
            pontos -= pontosPdds;
        }

        printf("Fim de jogo!\n");

        if(acertou){
                
            printf("\nVocê acertou em %d tentativas! \nPontos: %.2f\n", vzs, pontos);
        }else{
            printf("\nVocê Perdeu\n");
        }

    }   

}