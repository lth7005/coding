#include <stdio.h>
#define GAMES 5
int main245p(void)
{

	int a, b, c, d, e, i, j, k;
	char w, x, y, z;
	double n, m, o;


	int score[GAMES];

	for (i = 0, b = 0; i < GAMES; i++) { //b는 합계
		printf("enter %dst game score : ", i + 1);
		scanf_s("%d", &score[i]);
		b += score[i]; //이 문장은 이 for문 밖에서 다른 반복문으로 실행해도 된다. 입력에서 이미 score배열에 값이 저장됐기 때문.

	}

	n = b / GAMES; //n는 평균

	printf("average score : %f", n);

	printf("\n\n다음~!\n");
	return 0;
}