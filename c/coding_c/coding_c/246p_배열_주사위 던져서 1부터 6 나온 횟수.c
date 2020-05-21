#include <stdio.h>
#include <stdlib.h> //난수 발생하는 함수 있음
#include <time.h> //현재 시간(초)을 반환하는 함수 있음
#define REPEAT 10000
int main246p(void)
{

	int a, b, c, d, e, i, j, k;
	char w, x, y, z;
	double n, m, o;
	
	srand((unsigned int)time(0)); //prg실행할 때마다 새로운 난수 발생. time(0)은 1970년1월1일부터 지나온 시간(sec단위)을 반환한다.
	//만약 time()을 안쓰고 srand(??)를 쓴다면 ??의 숫자를 실행할 때마다 바꿔야 prg실행할 때마다 난수가 바뀐다.


	/*
	d = rand() % 6; //난수를 6으로 나눈 나머지를 a에 저장
	e = time(0);  //time(0)의 값을 확인한다.

	printf("%d\n", d);
	printf("%d\n", e);
	*/

	int dice[6] = { 0,0,0,0,0,0 }; // = { 0 }; 이렇게 하나만 써도 전체가 0으로 초기화 된다.


	for (;;) {
		printf("enter repeat num(1~%d) : ", REPEAT);
		scanf_s("%d", &a); //a는 주사위를 던지는 횟수
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




	printf("\n\n다음~!\n");
	return 0;
}