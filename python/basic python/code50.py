#s1,s2가 글자 길이가 같고 단 하나의 문자만 다르면 True, 나머지 False.
#사용자함수는 bool 결과로 반환할 것

def differ_by_one_char(s1,s2):
    if len(s1) != len(s2): return False
    else:
        i=0
        cou=0
        while i < len(s1):
            if s1[i] != s2[i]: cou+=1
            if cou > 1: return False
            i+=1
        return True

#main
word1=input('Enter word1 : ')
word2=input('Enter word2 : ')

if differ_by_one_char(word1,word2):
    print('(\'{}\', \'{}\') : differ by one character'.format(word1,word2))
else: print('(\'{}\', \'{}\') : not differ by one character'.format(word1,word2))
