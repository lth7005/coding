#include <stdio.h>
#include <limits.h>
int main(void)
{

	int a, b, c, d, e, i, j, k;
	char w, x, y, z;
	double n, m, o;

	do {
		printf("enter num:");
		scanf_s("%d", &a); //a�� �� �л� ��
	} while (a < 1 || a>25);
	
	for (i = 1, c = 0, d = 0, e = INT_MAX; i <= a; i++) {
		do {
			printf("enter %d student's score:", i);
			scanf_s("%d", &b); //b�� �� �л� ����
		} while (b < 0 || b>100);
		c += b; //c�� �հ�
		d = (d > b) ? d : b; //d�� �ִ�����
		e = (e < b) ? e : b; //e�� �ּ�����
	}

	n = c / a;

	printf("large score: %d, small score: %d, average score: %f", d, e, n);




	printf("\n\n����~!\n");
	return 0;
}