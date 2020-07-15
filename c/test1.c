
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{

	int repeat;
	printf("enter repeat num : ");
	scanf_s("%d", &repeat);

	int i;
	int coin[2] = { 0 };
	srand((unsigned int)time(0));

	for (i = 0; i < repeat; i++)
		rand() % 2 == 0 ? coin[0]++ : coin[1]++;

	printf("coin-F : %d, coin-B : %d\n", coin[0], coin[1]);

	printf("\n\n����~!\n");
	return 0;
}