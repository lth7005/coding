#include <stdio.h>
#define GAMES 5
int main245p(void)
{

	int a, b, c, d, e, i, j, k;
	char w, x, y, z;
	double n, m, o;


	int score[GAMES];

	for (i = 0, b = 0; i < GAMES; i++) { //b�� �հ�
		printf("enter %dst game score : ", i + 1);
		scanf_s("%d", &score[i]);
		b += score[i]; //�� ������ �� for�� �ۿ��� �ٸ� �ݺ������� �����ص� �ȴ�. �Է¿��� �̹� score�迭�� ���� ����Ʊ� ����.

	}

	n = b / GAMES; //n�� ���

	printf("average score : %f", n);

	printf("\n\n����~!\n");
	return 0;
}