#include <stdio.h>
int main209p(void)
{

	double c, f, x;
	int i;

	for (f = 0; f < 101; f += 10) {
		c = (f - 32) * 5 / 9;	//c에 저장하지 않고 printf문에서 바로 계산하고 출력하면 변수 하나로 프로그램 가능.
		printf("%6.2f F = %6.2f C\n", f, c);
	}





	printf("\n\n다음~!\n");
	return 0;
}