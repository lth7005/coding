#include <stdio.h>
int main209p(void)
{

	double c, f, x;
	int i;

	for (f = 0; f < 101; f += 10) {
		c = (f - 32) * 5 / 9;	//c�� �������� �ʰ� printf������ �ٷ� ����ϰ� ����ϸ� ���� �ϳ��� ���α׷� ����.
		printf("%6.2f F = %6.2f C\n", f, c);
	}





	printf("\n\n����~!\n");
	return 0;
}