
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int toss(void); //"앞이면 1, 뒤면 0을 반환하는 함수를 만드세요" 

int main300p(void)
{

	int repeat;
	printf("enter repeat num : ");
	scanf_s("%d", &repeat);

	int i, f, b;
	srand((unsigned int)time(0));

	for (i = 0, f = 0, b = 0; i < repeat; i++)
	{
		if (toss() == 1)
			f++;
		else
			b++;
	}

	printf("coin-F : %d, coin-B : %d\n", f, b);

	printf("\n\n다음~!\n");
	return 0;
}

int toss(void)
{
	int x;
	x = rand() % 2;
	if (x == 1)
		return 1;
	else
		return 0;
}