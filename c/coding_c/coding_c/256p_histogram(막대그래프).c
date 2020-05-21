#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define size 10
int main256p(void)
{

	int a, b, c, d, e, i, j, k;
	char w, x, y, z;
	double n, m, o;
	
	int nums[size];
	
	srand(time(0));
	
	for (i = 0; i < size; i++)
		nums[i] = rand() % 8 + rand() % 9; //0부터 15까지 난수로 저장

	printf("index value graph\n");
	for (i = 0; i < size; i++) {
		printf("%5d %5d ", i, nums[i]);
		for (j = 0; j < nums[i]; j++)
			printf("*");
		printf("\n");
	}



		


	printf("\n\n다음~!\n");
	return 0;
}