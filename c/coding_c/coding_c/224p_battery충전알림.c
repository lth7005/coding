//�������� 10���� �����̸� ��� �Ұ�, ������ �����ϰ� ����غ�����.

#include <stdio.h>
int main224p(void)
{

	int a, b, c, d, e, i, j, k;
	char w, x, y, z;
	double n, m, o;

	n = 3000; //���� battery
	o = 5000; //���� �Ϸ� battery


	printf("recent battary:%f\n", n); //full battery is 5000

	while(1) {
		printf("use + or charge - :");
		scanf_s("%lf", &m);
		n += m;
		if (n >= o) {
			n = o;
			printf("recent battery:%f\n", n);
			printf("battery is full\n");
		}
		else if (n > o * 0.1)
			printf("recent battery:%f\n", n);
		else if (n <= 0) { // ���� ���͸��� 0�̰ų� ������ ��
			n = 0;
			printf("recent battery:%f\n", n);
			printf("you need charge now\n");
			//break;
		}
		else { // o*0.1 >= n > 0 �� �� : ���� ���͸��� ������ 10%�����̰� 0���� Ŭ ��
			printf("recent battery:%f\n", n);
			printf("you need charge now\n");
			//break;
		}
	}
	


	printf("\n\n����~!\n");
	return 0;
}