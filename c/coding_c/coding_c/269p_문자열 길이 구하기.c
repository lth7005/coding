#include <stdio.h>
int main269p(void)
{
	//문자열 길이 구하기

	
	/*
	char s[10], i; //i는 문자형???!!

	printf("enter str : ");
	scanf_s("%s", s, sizeof(s));

	i = 0; //문자형으로 해놓고 왜 정수 0을 넣는 거지?
	while (s[i] != '\0') {
		i++;
		printf("%d", i);
	}

	printf("length : %d", i); 
	//그런데 정상적으로 i가 계산이 된다. 이상하게...
	*/
	
	
	char s[10];

	printf("enter str : ");
	scanf_s("%s", s, sizeof(s)); //비쥬얼 스튜디오 버전 문제로, scnaf_s()에서 입력받을 때는 입력받을 변수의 크기도 입력해줘야 한다고 한다.

	int i = 0;
	while (s[i] != '\0')
		i++;

	printf("length : %d", i);  //i+1이 아닌 이유는, 문자열의 길이에 NULL문자는 제외. abc의 길이 3으로.

	


	printf("\n\n다음~!\n");
	return 0;


}