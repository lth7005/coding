#include <stdio.h>
#define SIZE 10
int main261p(void)
{

	int a, b, c, d, e, i, j, k;
	char w, x, y, z;
	double n, m, o;
	
	int A[3][3] = { {2,3,0},{8,9,1},{7,0,5} };
	int B[3][3] = { {1,0,0}, {1,0,0}, {1,0,0} };
	int C[3][3];
	
	for (i = 0; i < 3; i++) {
		for (j = 0; j < 3; j++) {
			C[i][j] = A[i][j] + B[i][j];
			printf("%d ", C[i][j]);
		}
		printf("\n");
	}

		


	printf("\n\n´ÙÀ½~!\n");
	return 0;
}