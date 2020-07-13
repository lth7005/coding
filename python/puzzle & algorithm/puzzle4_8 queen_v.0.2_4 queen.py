# n x n 체스판에서 n개의 퀸을 놓는데 서로 공격할 수 없게 놓는 방법
# ex) 8x8 체스판에서 8개의 퀸을 서로 공격하지 않게 위치시킨다.  
# 1.같은 열 x 2.같은 행 x 3.같은 대각선 x
# 이 문제는 '완전탐색' 과 관련된다고 함

def fourqueen(n):

    x = list()
    y = [0,1,2,3]
    result = list()

    for i0 in y: #0
        print('__0__for__','/','i0:',i0,end=' / ')
        x.append(i0)
        print('x:',x)
        for i1 in y: #1
            print('__1__for__','/','i1:',i1,end=' / ')
            if diagnal(x,y,i1): print('x:',x) ; continue
            else: x.append(i1) ; print('x:',x)
            for i2 in y: #2
                print('__2__for__','/','i2:',i2,end=' / ')
                if diagnal(x,y,i2): print('x:',x) ; continue
                else: x.append(i2) ; print('x:',x)
                for i3 in y: #3
                    print('__3__for__','/','i3:',i3,end=' / ')
                    if diagnal(x,y,i3): print('x:',x) ; continue
                    else: x.append(i3) ; print('x:',x)
                    if len(x) == n: print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@') ; result.append(x.copy()) ; print(result) 
                    # result.append(x)로 하면 안된다. x가 수정되면 result 안의 x도 수정된다. 같은 메모리 주소이다.
                    x.remove(i3)
                x.remove(i2)
            x.remove(i1)
        x.remove(i0)

    return result

def diagnal(x, y, i):

    k = len(x)
    j = 0
    z = set(x)

    while k > 0:
        if x[j] - k in y: z.add(x[j] - k)
        if x[j] + k in y: z.add(x[j] + k)
        k -= 1
        j += 1
    print('z:',z,end=' / ')
    if i in z : 
        print('true',end=' / ')
        return True
    else:
        print('false',end=' / ')
        return False
    
#main
num = 4 #num = int(input('enter number n (n x n) : '))
answer = fourqueen(num)
for i in answer:
    print(i)
print(len(answer))
