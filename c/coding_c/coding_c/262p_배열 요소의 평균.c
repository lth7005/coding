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
	double aver = (double) sum / 4; //�ڷ��� ��ȯ -> (�Ǽ�) ���� / ���� -> �̸� ��ȣ�� ���� ����Ǿ� �Ǽ�/���� �� �ȴ�.
	printf("p2`s average is %f", aver); 

		


	printf("\n\n����~!\n");
	return 0;
}