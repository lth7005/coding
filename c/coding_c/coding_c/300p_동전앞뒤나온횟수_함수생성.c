
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int toss(void); //"���̸� 1, �ڸ� 0�� ��ȯ�ϴ� �Լ��� ���弼��" 

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

	printf("\n\n����~!\n");
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