#include <stdio.h>

//int int_max(int); //function prototype

void printf1(void)
{
	printf("-----------------------\n");
	printf("-----------------------\n");
}

int add1(int x, int y)
{
	int result;
	result = x + y;
	return result;
}

int add2(int x, int y)
{
	return x + y;
}

int square(int x)
{
	return x * x;
}

int int_large(int x, int y)
{
	return x > y ? x : y; // n = x > y ? x : y
}

double FtoC(int temp_f)
{
	double c;
	c = ((double)temp_f - 32) * 5 / 9;
	return c;
}

int main279p289p1(void)
{
	printf1();
	printf("æ»≥Á?\n");
	printf1();
	printf("hello!\n");
	
	int sum;
	sum = add1(2, 3);
	printf("sum : %d\n", sum);

	sum = add2(4, 5);
	printf("sum : %d\n", sum);

	sum = add2(123, 234);
	printf("sum : %d\n", sum);

	int k;
	k = square(10);
	printf("square : %d\n", k);
	
	k = int_large(8, 9);
	printf("large num : %d\n", k);






	printf("\n\n¥Ÿ¿Ω~!\n");
	return 0;



}