#Programming for the Puzzled -- Srini Devadas
#You Will All Conform
#Input is a vector of F's and B's, in terms of forwards and backwards caps
#Output is a set of commands (printed out) to get either all F's or all B's
#Fewest commands are the goal

'''
1.마지막 요청내용이 Person at position 11 flip your cap! 이 되도록
2.onepass를 수정해서 자연스러운 문장 나오게. 그리고 빈 리스트 입력되도 오류나지 않게
3.입장객 중에서 모자를 쓰지 않은 사람을 'H'라고 한다.
cap3=[f,f,b,h,b,f,b,b,b,f,h,f,f]
H는 모두 요청하지 않고 넘기기, cap3 입력하면 아래처럼 나오기
person in position 2 flip your cap! 그리고 2->4
person in position 6 through 8 flip your caps!
4.BWWWWWBWWWW 를 1B5W1B4W로 출력=인코딩함수
디코딩함수는 원래 문자열로.
인코딩과 디코딩은 단 한 번만 훑고 지나가서 결과를 출력
'''

caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F' ]
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F' ]
cap0 = []

def pleaseConformOpt(caps):
    #Initialization
    start = 0
    forward = 0
    backward = 0
    intervals = []

    caps = caps + ['END']

    #Determine intervals where caps are on in the same direction
    for i in range(1, len(caps)):
        if caps[start] != caps[i]:
            # each interval is a tuple with 3 elements (start, end, type)
            intervals.append((start, i - 1, caps[start]))
            
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i

    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2] == flip:
            #Exercise: if t[0] == t[1] change the printing!
            if t[0] == t[1]:
                print('Person at position', t[0], 'flip your cap!')  
            else:
                print ('People in positions', t[0], 'through', t[1], 'flip your caps!')
        

def pleaseConformOnepass(caps):
    caps = caps + [caps[0]]
    for i in range(1, len(caps)): # i를 0, i-1, i+1 과 비교. 즉, 3가지 경우.
        if caps[i] != caps[i-1]: #<-1 : i와 i-1>  다르면
            if caps[i] != caps[0]: #<0 : i와 0> 다르면 
                if caps[i] != caps[i+1]: #<+1 : i와 i+1> 다르면
                    print('Person at position', i, 'flip your cap!')  
                else: #<+1>같은면 <>실행
                    print('People in positions', i, end='')
            else: #2.2> i와 0이 같다면
                if 
                else: #'i-1까지 바꾸세요'
                    print(' through', i-1, 'flip your caps!')
        

# 0 0 0 0 0 0 1 1 1 1 0 0 0 0 

#pleaseConformOpt(caps)
#print('')
pleaseConformOnepass(caps)
