#include <stdio.h>
#include <limits.h>
int main230p(void)
{

	int a, b, c, d, e, i, j, k;
	char w, x, y, z;
	double n, m, o;

	for (;;) {
		printf("students num:");
		scanf_s("%d", &a); //a�� �л���, 1�̻� 25����
		if (a > 25 || a < 1) {
			printf("try again\n");
			continue;
		}
		else
			break;
	}

	for (i=1, c=0, d=0, e=INT_MAX; i<=a; i++) { //c�� �л��� ���� �հ�, d�� �ִ�, e�� �ּ�
		for (;;) {
			printf("enter %d student's score:", i);
			scanf_s("%d", &b); //b�� �� �л��� ���� ����, 0 �̻� 100 ����
			if (b < 0 || b>100) {
				printf("try again\n");
				continue;
			}
			else
				break;
		}
		c += b; // c�� �հ�
		printf("sum is %d\n", c);
		d = (d < b) ? b : d; // d�� �ִ�
		printf("largh num is %d\n", d);
		e = (e < b) ? e : b; // e�� �ּ�
		printf("small num is %d\n", e);
	}
	n = c / a; //n�� �л��� ��� ����

	printf("large score:%d, small score:%d, average:%.2f", d, e, n);




	printf("\n\n����~!\n");
	return 0;
}