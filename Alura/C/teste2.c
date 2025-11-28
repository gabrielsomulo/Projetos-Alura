#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int seg = time(0);
    srand(seg);

    int n1 = rand();
    int n2 = rand();

    printf("%d\n%d\n", n1, n2);
}

 