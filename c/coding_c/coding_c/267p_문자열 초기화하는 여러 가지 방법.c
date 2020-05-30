#include <stdio.h>
int main267p(void)
{
	

	char str1[4] = "abc"; // 마지막 인덱스에 NULL 문자가 자동으로 추가됨.
	char str2[4] = "abcdef"; // NULL문자 없이 문자만 저장.
	char str3[6] = "abc"; // 남는 인덱스에 모두 NULL문자가 자동으로 추가됨
	char str4[4] = { 'a', 'b', 'c', '\0' };
	char str5[4] = ""; // 모든 인덱스를 NULL 문자로 초기화.
	char str6[] = "abc"; // 자동으로 크기가 4로 설정됨. NULL문자도 추가됨. 가장 편리한 방법.

	//printf("%s\n", str2);

	printf("\n\n다음~!\n");
	return 0;
}