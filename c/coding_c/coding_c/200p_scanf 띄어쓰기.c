#include <stdio.h>
int main200(void)
{

	char a;

	do
	{
		printf("enter color:");
		scanf_s("%c", &a); //���⼭ "(���)%c �� ��� �������.
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