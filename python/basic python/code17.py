'''
영문이름 first name, last name 입력받기
firstn 첫글자랑 lastn 합쳐서 소문자 id 만들어주고 아래 출력해주기
Make a password as follows.
- Must be at least 8 letters
- Alphabet and numbers only
패스워드 입력받기, 패스워드 8자 이상, 영문자 또는 숫자 또는 섞어서.
맞는 패스워드면
Nice password 출력
8자 안되면 Must... 출력, 특수문자 들어가면 Al... 출력
'''

f_n = input('first name :')
f_l = input('last name :')
id = f_n[0].lower() + f_l.lower()
print('Your ID :', id)
print('''Make a password as follows.
- Must be at least 8 letters
- Alphabet and numbers only''')
ps = input('password :')
if len(ps) >= 8:
    if ps.isalnum():
        print('Nice password')
    else:
        print('Alphabet and numbers only')
elif ps.isalnum():
    print('Must be at least 8 letters')
else:
    print('''Must be at least 8 letters
Alphabet and numbers only''')
