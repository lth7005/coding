// 997711177 �� �Ҽ� (9��)
/*
��°����,
������ �Է� : ?
?�� �Ҽ� �Դϴ�/�ƴմϴ�
�Լ� is_prime() �����ϱ�
*/

#include <stdio.h>

void is_prime(long);

int main290p(void)
{

	long k;
	printf("enter num : ");
	scanf_s("%d", &k);

	is_prime(k);

	printf("\n\n����~!\n");
	return 0;
}

void is_prime(long x) // ��ȯ���� ��� ��ȯ�� �ڸ��� void
{
	int i, count;

	for (i = 1, count = 0; i <= x; i++) {
		count = x % i == 0 ? ++count : count + 0;
		if (count > 2)
			break;
		//printf("%d\n", i); //if�� �ȿ��� break �Ǹ� for������ ���ߴ��� Ȯ���ϴ� printf
	}

	count == 2 ? printf("%d is prime num\n", x) : printf("%d is not prime num\n", x);
	//��ȯ���� ����, ��¸� ���ִ� �Լ�
}