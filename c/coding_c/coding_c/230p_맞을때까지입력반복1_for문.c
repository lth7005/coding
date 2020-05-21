#include <stdio.h>
#include <limits.h>
int main230p(void)
{

	int a, b, c, d, e, i, j, k;
	char w, x, y, z;
	double n, m, o;

	for (;;) {
		printf("students num:");
		scanf_s("%d", &a); //a는 학생수, 1이상 25이하
		if (a > 25 || a < 1) {
			printf("try again\n");
			continue;
		}
		else
			break;
	}

	for (i=1, c=0, d=0, e=INT_MAX; i<=a; i++) { //c는 학생들 점수 합계, d는 최대, e는 최소
		for (;;) {
			printf("enter %d student's score:", i);
			scanf_s("%d", &b); //b는 각 학생의 점수 저장, 0 이상 100 이하
			if (b < 0 || b>100) {
				printf("try again\n");
				continue;
			}
			else
				break;
		}
		c += b; // c는 합계
		printf("sum is %d\n", c);
		d = (d < b) ? b : d; // d는 최대
		printf("largh num is %d\n", d);
		e = (e < b) ? e : b; // e는 최소
		printf("small num is %d\n", e);
	}
	n = c / a; //n은 학생들 평균 점수

	printf("large score:%d, small score:%d, average:%.2f", d, e, n);




	printf("\n\n다음~!\n");
	return 0;
}