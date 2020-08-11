'''
#퍼즐8. 누가 저녁파티에 오지 않게 될까
#참고사항 : 리스트 합치기, 완전탐색과 인코딩 조합
'''

#모든 조합 생성하기
#A,B,C,D,E 의 부분집합 생성하기 -> 원소 5개의 부분집합의 개수 = 2**n
#원소 n개에서 k를 포함하는 또는 포함하지 않는 부분집합의 개수 = 2**(n-k) 
#다섯개의 원소를 동그란 원 형태로 나열하고, 각 원소를 연결하는 직선을 그으면, 그 선들이 2개 원소를 선택하는 경우들
# 그 선이 1개이면 원소 2개를 선택하는 경우, 선이 2개면 원소 3개를 선택하는 경우, 선이 3개면 원소 4개를 선택하는 경우, 선이 4개면 원소 5개를 선택하는 경우
# 순서에 상관없이 -> [a,b] 와 [b,a] 는 서로 같은 경우로
# 그 선들 하나하나에 고유 번호 부여 -> ...
# 직선은 총 10개
# 직선 1개 선택 : 10가지, 2개 선택 : 

'''
def PrintAllCases(variable): # n개의 원소가 있는 집합의 부분집합(2**n개)을 출력하는 함수
    
    x = list('ABCDE')
    #y = ''
    y = list()
    z = list()
    k = ' '

    for i in range(len(x)):
        for k[i] in range(len(x)):


    for a in range(len(x)):
        y += x[a]
        for b in range(len(x)):
            y += [a,b]
            for c in range(len(x)):
                y += [a,b,c]
                for d in range(len(x)):
                    y += [a,b,c,d]

    print(z)
'''

#모든 경우의 수를 출력(변수는 a,b,c라고 가정)
#불대수 a`bc`처럼 출력하는데 프라임(`)이 붙은 변수는 생략하게.
#a,b,c 변수의 참, 거짓을 [[0,1], [0,1], [0,1]]로 표현
#불대수에서 정준형식의 최소항처럼 표현

def PrintAllCases(n):    #n은 변수의 개수 
    x = [[0,1]]*n    #[0,1]*3 -> [0,1,0,1,0,1]
    x_copy = x.copy()    #x_copy = x -> x_copy가 수정되면 x도 수정된다.
    y = list()

    #하나의 최소항을 만드는 반복문
    #각 최소항은 각각 고유번호를 갖고 있다.
    '''
    i = 1
    while 2**n >= 0: #각 최소항에 고유 번호 i가 할당됨
        for문
        i+=1
    '''
    for i in range(n):    
        for j in [0,1]:     #각 변수에 참, 거짓을 할당 #for j in [True, False]:도 가능?
            if j: x_copy[i] = j
            else: x_copy[i] =    

#variable = int(input('enter the number of variable :'))