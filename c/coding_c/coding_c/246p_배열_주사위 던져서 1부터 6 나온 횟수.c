#include <stdio.h>
#include <stdlib.h> //���� �߻��ϴ� �Լ� ����
#include <time.h> //���� �ð�(��)�� ��ȯ�ϴ� �Լ� ����
#define REPEAT 10000
int main246p(void)
{

	int a, b, c, d, e, i, j, k;
	char w, x, y, z;
	double n, m, o;
	
	srand((unsigned int)time(0)); //prg������ ������ ���ο� ���� �߻�. time(0)�� 1970��1��1�Ϻ��� ������ �ð�(sec����)�� ��ȯ�Ѵ�.
	//���� time()�� �Ⱦ��� srand(??)�� ���ٸ� ??�� ���ڸ� ������ ������ �ٲ�� prg������ ������ ������ �ٲ��.


	/*
	d = rand() % 6; //������ 6���� ���� �������� a�� ����
	e = time(0);  //time(0)�� ���� Ȯ���Ѵ�.

	printf("%d\n", d);
	printf("%d\n", e);
	*/

	int dice[6] = { 0,0,0,0,0,0 }; // = { 0 }; �̷��� �ϳ��� �ᵵ ��ü�� 0���� �ʱ�ȭ �ȴ�.


	for (;;) {
		printf("enter repeat num(1~%d) : ", REPEAT);
		scanf_s("%d", &a); //a�� �ֻ����� ������ Ƚ��
		if (a < 1 || a>REPEAT) {
			printf("try again\n");
			continue;
		}
		else
			break;
	}

	for (i = 0; i < a; i++) {
		dice[rand() % 6]++;
	}

	for (j = 0; j < 6; j++) {
		printf("%dst dice : %3d\n", j + 1, dice[j]);
	}




	printf("\n\n����~!\n");
	return 0;
}