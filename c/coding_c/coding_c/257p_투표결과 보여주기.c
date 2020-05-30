#include <stdio.h>
#define SIZE 10 //11로 정해서 인덱스 0번을 사용하지 않는 방법도 있다.
int main257p(void)
{

	int a, b, c, d, e, i, j, k;
	char w, x, y, z;
	double n, m, o;
	
	int s[SIZE] = { 0 };

	j = 0; //입력한 횟수

	do {
		printf("enter num(1~10, 0 is exit) : ");
		scanf_s("%d", &a);
		if (a > 0 && a <= SIZE)
			s[a - 1]++;
		else if (a == 0)
			break;
		else {
			printf("try again plz\n");
			continue;
		}
		j++;
	} while (2);

	printf("number of times : %d\n", j);
	printf("  num  count  \n");
	for (i = 0; i < SIZE; i++)
		printf("%5d%7d\n", i + 1, s[i]);
		


	printf("\n\n다음~!\n");
	return 0;
}