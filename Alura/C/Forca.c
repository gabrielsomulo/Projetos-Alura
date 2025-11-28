#include <stdio.h>
#include <string.h>
#include "Forca.h"
#include <time.h>
#include <stdlib.h>

//GCC (GNU Compiler Collection)
//gcc arquivo.c -o arquivo.out

int tentativas, falhas, errou, achou, randomico, qtd_palavras1, qtd_palavras2, quer;
char chute;
char chutes[26];
char palavra_secreta[20];
char nova_palavra[20];
FILE* f1;
FILE* f2;

void escolha_palavra(){
    //sprintf(palavra_Secreta, "AUDIO");

    f1 = fopen("C:\\Users\\gabri\\Alura\\C\\palavras.txt", "r");
    if(f1==0)
    {
        printf("Deu erro!!!");
        exit(1);

    }

    fscanf(f1, "%d", &qtd_palavras1);

    srand(time(0));
    randomico = rand() % qtd_palavras1;

    for (int i = 0; i <= randomico; i++)
    {
        fscanf(f1, "%s", palavra_secreta);
    }
    

    fclose(f1);
}

void mensagem(){
    printf("*****************\n");
    printf("  JOGO DA FORCA  \n");
    printf("*****************\n\n");
}

int ja_chutou(char letra){

    achou = 0;

    for (int j = 0; j < tentativas; j++)
    {
        if (chutes[j]==letra)
        {
            achou = 1;
            break;
        }
    }

    return achou;
}

void desenhar()
{   
printf("\n %s \n", (errou >= (int)(strlen(palavra_secreta)*0.2) ? " ( ) ":"  .  "));
printf("\n %s \n", (errou >= (int)(strlen(palavra_secreta)*0.4) ? "(---)":"  .  "));
printf("\n %s \n", (errou >= (int)(strlen(palavra_secreta)*0.6) ? "  |  ":"  .  "));
printf("\n %s \n", (errou >= (int)(strlen(palavra_secreta)*0.8) ? " | | ":"  .  "));
printf("\n %s \n", (errou >= (int)(strlen(palavra_secreta)*1) ? " . . ":"  .  "));


    for (int i = 0; i < strlen(palavra_secreta); i++)
    {
        if (ja_chutou(palavra_secreta[i])){
            printf("%c ", palavra_secreta[i]);  
        }
        else{
            printf(" _ ");
        }
    }
}

void imprimir(){
        printf("Qual a letra ? \n");
        scanf(" %c", &chute);

        chutes[tentativas] = chute;
        tentativas ++;       
}

int perdeu()
{
    falhas = 0;

    for (int i = 0; i < strlen(palavra_secreta); i++)
    {
        if(chute!=palavra_secreta[i])
        {
            ++falhas;
        }
    }

    if(falhas >= strlen(palavra_secreta)) ++errou;

    if(errou >= strlen(palavra_secreta)) return 1;

    return 0;
}

int ganhou()
{
    for (int i = 0; i < strlen(palavra_secreta); i++)
    {
        if (!ja_chutou(palavra_secreta[i])){
            return 0;
        }
    }
    
    return 1;
}

void adicionar_palavra(){
    printf("\n Voce deseja adicionar uma palavra? \n");
    scanf(" %d", &quer);

    if(quer == 1)
    {
        printf("Qual a nova palavra? \n");
        scanf(" %s", nova_palavra);

        f2 = fopen("C:\\Users\\gabri\\Alura\\C\\palavras.txt", "r+");
        if(f2==0)
        {
            printf("Deu erro!!!");
            exit(1);

        }

        // Qtd de palavras
        fscanf(f2, " %d", &qtd_palavras2);

        // Adição da nova palavra
        qtd_palavras2++;

        // Reposicionar ponteiro para o começo
        fseek(f2, 0, SEEK_SET);

        // Atualizar número de palavras
        fprintf(f2, "%d", qtd_palavras2);

        // Posicionar o ponteiro para o final
        fseek(f2, 0, SEEK_END);

        fprintf(f2, "\n%s", nova_palavra);

        fclose(f2);
    }

}

int main(){
    //Teste de Ponteiro com Array
    escolha_palavra();
    tentativas = 0;

    mensagem();

    do {
        desenhar();
        printf("\n\n");

        imprimir();
    }while(!ganhou() && !perdeu());

    if(ganhou()) printf("\nGanhou!!!\n\n");
    
    if(perdeu()) printf("\nPerdeu!!!\n\n");

    adicionar_palavra();
}


