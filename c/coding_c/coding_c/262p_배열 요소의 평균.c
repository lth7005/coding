#include <stdio.h>
int main262p(void)
{
	

	int p[3][4] = {
		{4,6,2,9},
		{7,8,3,7},
		{6,9,7,6}
	};
	
	int i, sum;
	for (i = 0, sum=0; i < 4; i++) {
		sum += p[2][i];
	}
	double aver = (double) sum / 4; //자료형 변환 -> (실수) 정수 / 정수 -> 이면 괄호가 먼저 수행되어 실수/정수 가 된다.
	printf("p2`s average is %f", aver); 

		


	printf("\n\n다음~!\n");
	return 0;
}