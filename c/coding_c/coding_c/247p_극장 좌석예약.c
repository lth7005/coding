#include <stdio.h>
#define SIZE 10
#define CLEAR 55
int main247p(void)
{

	int a, b, c, d, e, i, j, k;
	char w, x, y, z;
	double n, m, o;

	int seat[SIZE] = { 0 };

	for (i = 0; i < CLEAR; i++) printf("\n");

	for (;;) {
		printf("(if you want to exit, enter 0)");
		printf("\n=================================\n"); //33개
		for (i = 0; i < SIZE; i++)
			printf("  %d", i + 1);
		printf("\n---------------------------------\n");
		for (i = 0; i < SIZE; i++)
			printf("  %d", seat[i]);
		printf("\n=================================\n");
		printf("enter the seat num : ");
		scanf_s("%d", &a); //a는 입력된 좌석 번호
		printf("\n");
		if (a == 0) 
			break;
		else if (a < 0 || a>SIZE) {
			for (i = 0; i < CLEAR; i++) printf("\n");
			printf("***plz enter num of 1 to 10. try again***\n\n");
			continue;
		}
		else if (seat[a - 1] == 1) {
			for (i = 0; i < CLEAR; i++) printf("\n");
			printf("***it's already reserved. try again plz.***\n\n");
			continue;
		}
		else {
			for (i = 0; i < CLEAR; i++) printf("\n");
			seat[a - 1] = 1;
		}
		
		
	}



	printf("\n\n다음~!\n");
	return 0;
}