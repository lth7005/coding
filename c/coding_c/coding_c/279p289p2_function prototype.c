#include <stdio.h>

int int_large(int, int);
void printf1(); // �� �Լ������� ���� main �ȿ��� �ٷ� printf1(); �ص� �Լ��� ����. ������ �˻�?�ϱ� ���� �� �Լ� ������ ���ٰ� ��.
double FtoC(int);

int main279p289p2(void)
{
	printf1();
	printf("�ȳ�?\n");
	
	printf("hello!\n");
	
	printf("large num : %d\n", int_large(987, 978));

	/*
	//288p
	int a, b;
	printf("enter two num : ");
	scanf_s("%d %d", &a, &b);

	printf("large num : %d\n", int_large(a, b));
	*/

	
	//289p
	int temp_f;
	printf("enter temp F : ");
	scanf_s("%d", &temp_f);
	
	printf("%d F is %.2f", temp_f, FtoC(temp_f));
	/**/


	printf("\n\n����~!\n");
	return 0;



}

/*
//�̷��� main ��� �Ʒ� �Լ��� �����ص� �ǳ�?
double FtoC(int temp_f)
{
	double c;
	c = ((double)temp_f - 32) * 5 / 9;
	return c;
}
*/