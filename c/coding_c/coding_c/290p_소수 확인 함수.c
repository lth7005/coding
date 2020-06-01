// 997711177 은 소수 (9억)
/*
출력결과는,
정수를 입력 : ?
?는 소수 입니다/아닙니다
함수 is_prime() 정의하기
*/

#include <stdio.h>

void is_prime(long);

int main290p(void)
{

	long k;
	printf("enter num : ");
	scanf_s("%d", &k);

	is_prime(k);

	printf("\n\n다음~!\n");
	return 0;
}

void is_prime(long x) // 반환값이 없어서 반환형 자리에 void
{
	int i, count;

	for (i = 1, count = 0; i <= x; i++) {
		count = x % i == 0 ? ++count : count + 0;
		if (count > 2)
			break;
		//printf("%d\n", i); //if문 안에서 break 되면 for문까지 멈추는지 확인하는 printf
	}

	count == 2 ? printf("%d is prime num\n", x) : printf("%d is not prime num\n", x);
	//반환값이 없는, 출력만 해주는 함수
}