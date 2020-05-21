#8주차 과제
'''
두 수를 입력 받아 덧셈값을 출력하는 함수를 만드시오.
'''

def print_addition(num1,num2):
    num = num1 + num2    #프로그램 종료 후 print(num) 은 NameError 발생
    print('두 수의 덧셈값은', num, '입니다.')

if __name__ == '__main__':
    print('두 수의 덧셈값을 알려드립니다.')
    num1 = int(input('첫 번째 정수를 입력해주세요 : '))
    num2 = int(input('두 번째 정수를 입력해주세요 : '))

    print_addition(num1,num2)    #이 함수의 반환값은 없습니다.
                                 
