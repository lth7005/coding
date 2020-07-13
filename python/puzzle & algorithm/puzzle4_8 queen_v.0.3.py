# n x n 체스판에서 n개의 퀸을 놓는데 서로 공격할 수 없게 놓는 방법
# ex) 8x8 체스판에서 8개의 퀸을 서로 공격하지 않게 위치시킨다.  
# 1.같은 열 x 2.같은 행 x 3.같은 대각선 x
# 이 문제는 '완전탐색' 과 관련된다고 함

def eightqueen(n):

    x = list()
    y = [0,1,2,3,4,5,6,7]
    result = list()

    for i0 in y: #0
        x.append(i0)
        for i1 in y: #1
            if diagnal(x,y,i1): continue
            else: x.append(i1)
            for i2 in y: #2
                if diagnal(x,y,i2): continue
                else: x.append(i2)
                for i3 in y: #3
                    if diagnal(x,y,i3): continue
                    else: x.append(i3)
                    for i4 in y: #4
                        if diagnal(x,y,i4): continue
                        else: x.append(i4)
                        for i5 in y: #5
                            if diagnal(x,y,i5): continue
                            else: x.append(i5)
                            for i6 in y: #6
                                if diagnal(x,y,i6): continue
                                else: x.append(i6)
                                for i7 in y: #7
                                    if diagnal(x,y,i7): continue
                                    else: x.append(i7)
                                    
                                    if len(x) == n: result.append(x.copy())
                                    # result.append(x)로 하면 안된다. x가 수정되면 result 안의 x도 수정된다. 같은 메모리 주소이다.
                                    x.remove(i7)
                                x.remove(i6)
                            x.remove(i5)
                        x.remove(i4)
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
    if i in z : return True
    else: return False
    
#main
num = 8 #num = int(input('enter number n (n x n) : '))
answer = eightqueen(num)
for i in answer:
    print(i)
print(len(answer))

'''
어떤 기능을 사용해서 코딩할지 막막할 땐
표를 직접 그려서 실행과정(사고 과정)을 전부 하나씩 연필로 적어볼 것.
내가 무엇을 해야할지 보일지도?! 
'''