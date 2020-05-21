#encrypt()함수는 하나의 문자열 입력받고 암호화한 문자열로 변환함
#e함수에 입력문자와 사전 code를 함께 넘김, 암호화 문자열을 반환

def encrypt(msg, code):
    #원문 msg와 암호코드 code를 입력받아서 암호문을 만들어 반환
    x=''
    for a in msg:
        x+=code[a]
    return x

#main
crypt_code = {'a': 'g', 'b': 'r', 'c': 'q', 'd': 'i', 'e': 'u',
              'f': 'e', 'g': 'w', 'h': 'n', 'i': 'd', 'j': 'l',
              'k': 'v', 'l': 't', 'm': 'f', 'n': 's', 'o': 'o',
              'p': 'a', 'q': 'k', 'r': 'x', 's': 'm', 't': 'p',
              'u': 'y', 'v': 'b', 'w': 'j', 'x': 'z', 'y': 'c',
              'z': 'h'}

plain_msg=input('Enter plain text : ')
encrypt_msg=encrypt(plain_msg, crypt_code)
print('crypted message :', encrypt_msg)

