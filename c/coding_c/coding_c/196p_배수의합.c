#include <stdio.h>
int main196p(void)
{
	int x, i, result;

	printf("enter num:");
	scanf_s("%d", &x);

	i = 0; result = 0;

	while (i * x <= 100)
	{
		result +=  i * x;
		i++;
	}
	printf("result:%d", result);






	printf("\n");
	printf("´ÙÀ½!\n");
	return 0;

}