'''
Enter input : 0
fibonacci number of 0 : 0
'''

m = int(input('Enter input :'))
n = m -2

i = 1
x = 1 #홀수방
y = 1 #짝수방 

if m <= 2:
    import sys
    print('fibonacci number of {} : {}'.format(m, 1))
    sys.exit(0)

while i <= n:
    
    if i % 2 == 1:  #n 홀수
        x += y
    else:   #n 짝수
        y += x
    i += 1

if n % 2 == 1:
    
    print('fibonacci number of {} : {}'.format(m, x))
else:
    
    print('fibonacci number of {} : {}'.format(m, y))

#print('fibonacci number of {} : {}'.format(입력, 출력)
