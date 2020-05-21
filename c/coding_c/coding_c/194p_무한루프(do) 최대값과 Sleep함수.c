#include <stdio.h>
#include <windows.h>
int main1942p(void)
{
	
	int max_int = 0, flag = 1, a = 0;

	do
	{
		printf("enter num:");
		scanf_s("%d", &a);
		Sleep(500); //1000ms = 1sec
		if (a == 0)
			flag = 0;
		else
			max_int = (max_int >= a) ? max_int : a;
	} while (flag == 1);

	printf("large num is %d", max_int);

	

	


	printf("\n");
	printf("¥Ÿ¿Ω!\n");
	return 0;
}