//충전상태 10프로 이하이면 사용 불가, 충전만 가능하게 출력해보세요.

#include <stdio.h>
int main224p(void)
{

	int a, b, c, d, e, i, j, k;
	char w, x, y, z;
	double n, m, o;

	n = 3000; //남은 battery
	o = 5000; //충전 완료 battery


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
		else if (n <= 0) { // 남은 배터리가 0이거나 음수일 때
			n = 0;
			printf("recent battery:%f\n", n);
			printf("you need charge now\n");
			//break;
		}
		else { // o*0.1 >= n > 0 일 때 : 남은 배터리가 완충의 10%이하이고 0보다 클 때
			printf("recent battery:%f\n", n);
			printf("you need charge now\n");
			//break;
		}
	}
	


	printf("\n\n다음~!\n");
	return 0;
}