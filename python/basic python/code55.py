'''
저장된 이메일 주소를 하나씩 읽어서 유효한 주소인지 판단하는 프로그램,
is_valid()라는 함수를 이용하여 인수로 넘기는 이메일 주소가 유효한 주소면,
True를 반환하고, 그렇지 않으면 False를 반환.
유효한 이메일 주소의 조건은
1.이메일 주소는 10글자 이상이어야 함
2.@는 반드시 한 개만 있어야 함
3.영문자로 시간해야 함
----
***@***     : True
*@***       : False
'''
def is_valid(line):
    #1번 line=line.strip()
    if len(line) < 10: return False
    elif not line[0].isalpha(): return False
    elif line.count('@') > 1 or line.count('@') == 0: return False
    else: return True

#main
f=open('55_email.txt','r')
for line in f:
    line=line.strip() #2번
    y=is_valid(line)
    print('{:<25} : {}'.format(line,y))

#line=line.strip() 이걸 2번에 쓰지 않고 1번에 써서 결과가 이상하게 나옴
#f.close() 빼먹
