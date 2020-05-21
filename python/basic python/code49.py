def unzip(s):
    #s를 숫자만큼 문자들을 반복하여 새로운 문자열을 만들어 반환
    x=''
    print('함수로 받은 문자열',s)
    print('문자열 길이',len(s))
    for a in range(int(len(s)/2)):
        print('시작번호',a)
        x+=s[2*a+1]*int(s[2*a])
    print('문자열 함수 결과', x)
    return x

#main

S=['9a5b1c', '2m4n', '1x5y3z','3o']

for string in S:
    new_string=unzip(string)
    print(string, ':', new_string)

'''
2m4n : mmnnnn
3o : ooo
'''
