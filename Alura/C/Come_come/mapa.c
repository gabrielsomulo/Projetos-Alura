#include <stdio.h>
#include <stdlib.h>
#include "mapa.h"

FILE* f;

void encontra_mapa(MAPA *M, POSICAO *p, char c)
{
    for (int i = 0; i < m->linhas; i++)
    {
        for (int j = 0; j < m->colunas; j++)
        {
            if(m->mapa[i][j] == c)
            {
                p->x=i;
                p->y=j;
                break;
            }
        }
        
    }
}

void  liberar_mapa( MAPA *m){
    for (int i = 0; i < m->linhas; i++)
    {
        free(m->mapa[i]);
    }  
    free(m->mapa);
}

void alocar_mapa(MAPA *m)
{
    m->mapa = malloc(sizeof(char*) * m->linhas);
    for (int i = 0; i < m->linhas; i++)
    {
        m->mapa[i] = malloc(sizeof(char) * (m->colunas+1));
    }
    
}

void ler_mapa(MAPA *m){
    f = fopen("C:\\Users\\gabri\\Alura\\C\\Come_come\\mapa.txt", "r");

    if(f==0)
    {
        printf("erro");
        exit(1);
    }

    fscanf(f, "%d %d", &(m->linhas), &(m->colunas));
    printf("%d %d \n\n", m->linhas, m->colunas);

    alocar_mapa(m);

    for (int i = 0; i <= 11; i++)
    {
        fscanf(f, "%s", m->mapa[i]);
    }

    fclose(f);
}

void imprimir_mapa(MAPA *m)
{
    for (int i = 0; i <= 11; i++)
    {
        printf("%s\n", m->mapa[i]);
    }
}