#include <stdio.h>

int square2(int x, int y)
{
	
	int i, k;
	k = x;
	for (i = 0; i < y-1; i++) 
		x *= k;
	return x;
	/*
	int i;
	for (i = 0; i < y; i++)
		x *= x; // x는 4라면, 1) x= 4*4, 2) x= 16 * 16 ...
	return x;
	*/
}



int main286p(void)
{

	int a,b ;
	printf("enter num : ");
	scanf_s("%d %d", &a, &b);

	int c;
	c = square2(a, b);
	printf("%d^%d = %d\n", a, b, c);
	




	printf("\n\n다음~!\n");
	return 0;



}