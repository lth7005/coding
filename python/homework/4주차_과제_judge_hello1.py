# 4주차 과제 1번
'''
'Hello, world!' 두 개를 각 줄에 출력하는 프로그램을 만드세요
(대소문자 구분과 띄어쓰기가 정확해야 합니다).
정답에는 출력 결과를 만족하는 전체 소스 코드를 입력해야 합니다.

파일이름: judge_hello.py

결과:
Hello, world!
Hello, world!

'''

print("Hello, world!\n"*2, end="")


# 4주차 과제 2번
'''
세개의 수를 입력하여 평균을 구하는 코드를 작성하시오. 
변수 num1=3, num2= 4, num3=7 이라할 때,
세 수의 평균을 계산하는 코드를 작성하시오. 
'''

num1 = 3
num2 = 4
num3 = 7

sum_num = (num1+num2+num3)/3

print('세 수의 평균은 약 %0.1f 입니다.' %sum_num)
