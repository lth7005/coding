#include <stdio.h>
#define SIZE 10 //11�� ���ؼ� �ε��� 0���� ������� �ʴ� ����� �ִ�.
int main257p(void)
{

	int a, b, c, d, e, i, j, k;
	char w, x, y, z;
	double n, m, o;
	
	int s[SIZE] = { 0 };

	j = 0; //�Է��� Ƚ��

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
		


	printf("\n\n����~!\n");
	return 0;
}