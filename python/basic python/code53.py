f=open('53_word.txt','r')
word=input('Enter word to test anagram : ')
#print('\n') 틀림, 아래처럼 할 
print('\n',end='') #또는 print(''), print()는 출력 후 엔터 입력됨
anag_cou=0
for line in f:
    line=line.strip()
    differ_cou=0 #이 코드 잊음
    for w in word:
        if w not in line: differ_cou=1 
    if differ_cou == 0 and len(word)==len(line):
        anag_cou+=1
        print(line)
print('-'*15)
print('There are %d anagrams'%anag_cou)

#def함수 사용해서 다시 해볼 것.
