'''
섭씨온도를 화씨 CtoF함수, 화씨를 섭씨 FtoC함수, 를 이용해서 바꾸는 코딩,
c, C, f, F 이외 문자 입력 시, 잘못된 입력입니다 출력하고 끝냄
화씨F = (9/5*섭씨)+32, 섭씨C=(화씨-32)*5/9

섭씨온도를 화씨로 바꾸려면 C또는 c를 입력하시오.
화씨온도를 섭씨로 바꾸려면 F또는 f를 입력하시오.

선택 ---> 0
섭씨온도를 입력하시오 : 0.00
섭씨온도 0.00도는 화씨 0.00도입니다.
'''

def temp(choice,t1):
    if choice == 'c': t=(9/5*t1)+32
    else: t=(t1-32)*5/9
    return t
#main
print('섭씨온도를 화씨로 바꾸려면 C또는 c를 입력하시오.')
print('화씨온도를 섭씨로 바꾸려면 F또는 f를 입력하시오.')
choice=input('선택 ---> : ')
choice=choice.lower()
if choice not in 'cf': #if choice not in ['c','f']: 또는 if choice != 'c' and choice != 'f':
    print('잘못된 입력입니다.')
    import sys
    sys.exit()
elif choice == 'c': a,b=('섭씨', '화씨')
else: a,b=('화씨','섭씨')
t1=float(input('%s온도를 입력하시오 : ' %a))
t2=temp(choice, t1)
print('{}온도 {:0.2f}도는 {} {:0.2f}도입니다.'.format(a,t1,b,t2))
