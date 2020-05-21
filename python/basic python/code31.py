'''하나의 양의 정수 입력받고, 그 수가 완전제곱수인지 판단
for문과 range함수 사용'''

n = int(input('Enter n : '))
if n == 1:
    print('1 is not perfect square number')
else: #n > 1일 경우
    for x in range(1,n+1):
        if x*x == n:
            print('{} is perfect square of {}'.format(n, x))
            break
        elif x*x > n:
            print('{} is not perfect square number'.format(n))
            break
            
