
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 45

int main299p(void)
{

	int i;

	srand((unsigned int)time(0));

	for (i = 0; i < 6; i++)
		printf("%d ", 1 + rand() % MAX);
	

	printf("\n\n´ÙÀ½~!\n");
	return 0;
}