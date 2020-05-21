#include <stdio.h>
#include <math.h>
int main228p(void)
{

	int a, b, c, d, e, i, j, k;
	char w, x, y, z;
	double n, m, o;

	for (a = 1; a < 100; a++) 
		for (b = 1; b < 100; b++)
			for (c = 1; c < 100; c++)
				if (pow(c, 2) == pow(a, 2) + pow(b, 2))
					printf("[%2d %2d %2d]\n", a, b, c);


	printf("\n\n´ÙÀ½~!\n");
	return 0;
}