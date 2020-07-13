import copy

a = list()
b = list()

for i in [1,2,3]:
     a.append(i)
     if i % 2 == 0: #참인 경우는 i = 2인 경우 뿐 
          b.append(a)
          print('a의 주소   :',id(a))
          print('b[0]의 주소:',id(b[0]))
          print('a의 주소와 b[0]의 주소는 같다? :', id(a) == id(b[0])  )
     a.remove(i)
print('b:',b)

d = c = [0,1,2]
print('c와 d의 주소는 같다? : ', id(c) == id(d) )
c.remove(2)
print('c:',c)
print('d:',d)


'''
import copy
y = copy.deepcopy(x)
로 해결 가능
'''
          