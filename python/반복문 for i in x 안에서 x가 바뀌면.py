
#for문에서 참조하는 리스트의 값이 바뀌면?
#반복문에서 참조하는 방법은 인덱스 번호

x = list()
y = list()
z = [0,1,2,3]

count = 0
for a in z:
     print('z:',z)
     print('index:',count,'a:',a)
     z.remove(a)
     for b in z:
          print('b:', b, end=' ')
     print()
     z.append(a)
     count += 1