#include <stdio.h>
#include <limits.h>
int main(void)
{

	int a, b, c, d, e, i, j, k;
	char w, x, y, z;
	double n, m, o;

	do {
		printf("enter num:");
		scanf_s("%d", &a); //a는 총 학생 수
	} while (a < 1 || a>25);
	
	for (i = 1, c = 0, d = 0, e = INT_MAX; i <= a; i++) {
		do {
			printf("enter %d student's score:", i);
			scanf_s("%d", &b); //b는 각 학생 점수
		} while (b < 0 || b>100);
		c += b; //c는 합계
		d = (d > b) ? d : b; //d는 최대점수
		e = (e < b) ? e : b; //e는 최소점수
	}

	n = c / a;

	printf("large score: %d, small score: %d, average score: %f", d, e, n);




	printf("\n\n다음~!\n");
	return 0;
}