#include <stdio.h>
int mainbbb(void)
{
	

	char s[10], i;

	printf("enter str : ");
	scanf_s("%s", s, sizeof(s));

	i = 0;
	while (s[i] != '\0')
		i++;

	printf("length : %d", i);
	
	
	
	return 0;
}