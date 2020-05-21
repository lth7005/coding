#include <stdio.h>
#include<math.h>
int main216p(void)
{
	
	int i, a, result;

	printf("enter num:");
	scanf_s("%d", &a);

	for (result = 0,  i = 1; i < a + 1; i++) {
		result += pow(i, 3);
	}


	printf("result is %d", result);


	printf("\n\n´ÙÀ½~!\n");
	return 0;
}