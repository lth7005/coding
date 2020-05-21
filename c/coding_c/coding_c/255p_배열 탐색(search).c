#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main255p(void)
{

	int a, b, c, d, e, i, j, k;
	char w, x, y, z;
	double n, m, o;
	

	int num[8];

	srand((int)time(0));
	
	for (i = 0; i < 8; i++) {
		num[i] = rand() % 10;
		printf("index<%d> %d,", i, num[i]);
	}
	printf("\n");

	printf("enter num 1 to 9 : ");
	scanf_s("%d", &a);

	for (i = 0, b=0; i < 8; i++) {
		if (num[i] == a) {
			printf(" index<%d>", i);
			b = 1;
		}
	}
	printf("\n");

	if (b==0)
		printf("not exist\n");
		


	printf("\n\n¥Ÿ¿Ω~!\n");
	return 0;
}