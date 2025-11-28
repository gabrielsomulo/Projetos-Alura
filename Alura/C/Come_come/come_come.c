#include <stdio.h>
#include <stdlib.h>
#include "come_come.h"
#include "mapa.h"


MAPA m;

FILE* f;

POSICAO heroi;


int acabou()
{
    return 0;
}

void move(char direcao)
{

    if( direcao != ESQUERDA &&
        direcao != CIMA &&
        direcao != DIREITA &&
        direcao != BAIXO &&) return;
    
    int proximo_x = heroi.x;
    int proximo_y = heroi.y;

    switch (direcao)
    {
    case ESQUERDA:
        proximo_y--;
        break;
    
    case CIMA:
        proximo_x--;
        break;
    case BAIXO:
        proximo_x++;
        break;

    case DIREITA:
        proximo_y++;
        break;

    }

    if(proximo_x >= m.linhas) return;
    if(proximo_y >= m.colunas) return;
    if(m.mapa[proximo_x][proximo_y] != CHAO) return;

    m.mapa[proximo_x][proximo_y] = PERSONAGEM;
    m.mapa[heroi.x][heroi.y] = CHAO;
    heroi.x = proximo_x;
    heroi.y = proximo_y;
}

int main(){
    ler_mapa(&m);
    encontra_mapa(&m, &heroi, PERSONAGEM);

    do
    {
        imprimir_mapa(&m);

        char comando;
        scanf(" %c", &comando);
        move(comando);

    } while (!acabou());
    

    liberar_mapa(&m);
    

}