#include <stdio.h>
int main267p(void)
{
	

	char str1[4] = "abc"; // ������ �ε����� NULL ���ڰ� �ڵ����� �߰���.
	char str2[4] = "abcdef"; // NULL���� ���� ���ڸ� ����.
	char str3[6] = "abc"; // ���� �ε����� ��� NULL���ڰ� �ڵ����� �߰���
	char str4[4] = { 'a', 'b', 'c', '\0' };
	char str5[4] = ""; // ��� �ε����� NULL ���ڷ� �ʱ�ȭ.
	char str6[] = "abc"; // �ڵ����� ũ�Ⱑ 4�� ������. NULL���ڵ� �߰���. ���� ���� ���.

	//printf("%s\n", str2);

	printf("\n\n����~!\n");
	return 0;
}