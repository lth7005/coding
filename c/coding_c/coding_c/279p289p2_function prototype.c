#include <stdio.h>

int int_large(int, int);
void printf1(); // 이 함수원형을 빼고 main 안에서 바로 printf1(); 해도 함수는 사용됨. 컴파일 검사?하기 위해 이 함수 원형을 쓴다고 함.
double FtoC(int);

int main279p289p2(void)
{
	printf1();
	printf("안녕?\n");
	
	printf("hello!\n");
	
	printf("large num : %d\n", int_large(987, 978));

	/*
	//288p
	int a, b;
	printf("enter two num : ");
	scanf_s("%d %d", &a, &b);

	printf("large num : %d\n", int_large(a, b));
	*/

	
	//289p
	int temp_f;
	printf("enter temp F : ");
	scanf_s("%d", &temp_f);
	
	printf("%d F is %.2f", temp_f, FtoC(temp_f));
	/**/


	printf("\n\n다음~!\n");
	return 0;



}

/*
//이렇게 main 블록 아래 함수를 정의해도 되나?
double FtoC(int temp_f)
{
	double c;
	c = ((double)temp_f - 32) * 5 / 9;
	return c;
}
*/