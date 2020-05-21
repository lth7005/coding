#include <stdio.h>
int main200(void)
{

	char a;

	do
	{
		printf("enter color:");
		scanf_s("%c", &a); //여기서 "(띄고)%c 로 써야 정상출력.
	} while (a != 'r' && a != 'y' && a != 'g');

	switch (a)
	{
	case 'r':
		printf("stop!");
		break;
	case 'y':
		printf("be careful!");
		break;
	case 'g':
		printf("go!");
		break;
	}

	return 0;

}