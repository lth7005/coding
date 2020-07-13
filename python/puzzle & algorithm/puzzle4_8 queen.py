# n x n 체스판에서 n개의 퀸을 놓는데 서로 공격할 수 없게 놓는 방법
# ex) 8x8 체스판에서 8개의 퀸을 서로 공격하지 않게 위치시킨다.  
# 1.같은 열 x 2.같은 행 x 3.같은 대각선 x

'''
프로그램 실행 예시  
'''

def eightqueen(n):

    x = list()
    y = [0,1,2,3,4,5,6,7]
    result = list()

    for i0 in range(n):
        print('i0:', i0)
        w = y.index(i0) ; x.append(i0) ; y.remove(i0)
        print('x:',x) ; print('y:',y)
        for i1 in y:
            print('i1:', i1)
            if diagnal(x,y,i1): continue            
            else: w = y.index(i1) ; x.append(i1) ; y.remove(i1)
            print('x:',x) ; print('y:',y)
            for i2 in y:
                print('i2:',i2)
                if diagnal(x,y,i2): continue            
                else: w = y.index(i2) ; x.append(i2) ; y.remove(i2)
                print('x:',x) ; print('y:',y)
                for i3 in y:
                    print('i3:',i3)
                    if diagnal(x,y,i3): continue            
                    else: w = y.index(i3) ; x.append(i3) ; y.remove(i3)
                    print('x:',x) ; print('y:',y)
                    for i4 in y:
                        print('i4:',i4)
                        if diagnal(x,y,i4): continue            
                        else: w = y.index(i4) ; x.append(i4) ; y.remove(i4)
                        print('x:',x) ; print('y:',y)
                        print(x) ; print(y) ; break
                        for i5 in y:
                            print('i5:',i5)
                            if diagnal(x,y,i5): continue            
                            else: w = y.index(i5) ; x.append(i5) ; y.remove(i5)
                            print('x:',x) ; print('y:',y)
                            for i6 in y:
                                print('i6:',i6)
                                if diagnal(x,y,i6): continue            
                                else: w = y.index(i6) ; x.append(i6) ; y.remove(i6)
                                print('x:',x) ; print('y:',y)
                                for i7 in y:
                                    print('i7:',i7)
                                    if diagnal(x,y,i7): continue            
                                    else: w = y.index(i7) ; x.append(i7) ; y.remove(i7)
                                    print('x:',x) ; print('y:',y)                                    
                                    if len(x) == n: 
                                        #print('@:', x)
                                        result.append(x)
                                    x.remove(i7) ; y.insert(w,i7)
                                x.remove(i6) ; y.insert(w,i6)
                            x.remove(i5) ; y.insert(w,i5)
                        x.remove(i4) ; y.insert(w,i4)
                    x.remove(i3) ; y.insert(w,i3)
                x.remove(i2) ; y.insert(w,i2)
            x.remove(i1) ; y.insert(w,i1)
        x.remove(i0) ; y.insert(w,i0)
    
    print(result)


def diagnal(x, y, i):

    k = len(x)
    j = 0
    z = list()

    while k > 0:
        if x[j] - k in y: z.append(x[j] - k)
        if x[j] + k in y: z.append(x[j] + k)
        k -= 1
        j += 1
    
    if i in z : 
        return True
    else :
        return False
    
#main
num = int(input('enter number n (n x n) : '))
eightqueen(num)
