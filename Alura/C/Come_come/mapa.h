struct mapa 
{
 char** mapa;
 int linhas, colunas;
};

typedef struct mapa MAPA;


struct posicao
{
    int x, y;
}

typedef struct posicao POSICAO

void liberar_mapa(MAPA *m);
void ler_mapa(MAPA *m);
void alocar_mapa(MAPA *m);
void imprimir_mapa(MAPA *m);
void encontra_mapa(MAPA *m, POSICAO *p, char c);