#include <stdio.h>
int main269p(void)
{
	//���ڿ� ���� ���ϱ�

	
	/*
	char s[10], i; //i�� ������???!!

	printf("enter str : ");
	scanf_s("%s", s, sizeof(s));

	i = 0; //���������� �س��� �� ���� 0�� �ִ� ����?
	while (s[i] != '\0') {
		i++;
		printf("%d", i);
	}

	printf("length : %d", i); 
	//�׷��� ���������� i�� ����� �ȴ�. �̻��ϰ�...
	*/
	
	
	char s[10];

	printf("enter str : ");
	scanf_s("%s", s, sizeof(s)); //����� ��Ʃ��� ���� ������, scnaf_s()���� �Է¹��� ���� �Է¹��� ������ ũ�⵵ �Է������ �Ѵٰ� �Ѵ�.

	int i = 0;
	while (s[i] != '\0')
		i++;

	printf("length : %d", i);  //i+1�� �ƴ� ������, ���ڿ��� ���̿� NULL���ڴ� ����. abc�� ���� 3����.

	


	printf("\n\n����~!\n");
	return 0;


}