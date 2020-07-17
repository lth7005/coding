#라이브러리를 사용하지 않고 코딩해보자 :)

'''
#퍼즐 5번째 "제발 유리 구슬이 깨지길"
#문제 : 128층인 상하이 타워에서 유리구슬을 떨어뜨렸을 때 깨지지 않는 가장 높은 층을 찾아내기
#문제 설명: 
유리구슬의 단단한 정도를 알아내기 위해 
어떤 건물에서 유리구슬을 떨어뜨려 깨지지 않는 가장 높은 층수를 찾으려고 한다.
어떤 층에서 깨지지 않으면 그 아래의 층수에서는 절대 깨지지 않는다.
어떤 층에서 깨지면 그 위의 층수에서는 항상 깨진다.
그리고 유리구슬은 한 번 깨지면 다시 사용할 수 없다.
최대 층수를 알아야하기 때문에, 만약 100층인 건물의 50층에서 떨어뜨려서 깨진다면
51층부터 100층까지 깨진다는 것은 알 수 있지만 그 아래 층수 중에서 몇 층까지 견디는지를 알 수가 없다. 
가장 정확한 방법은 1층부터 한 층씩 던져보는 방법이다.
여기 구슬이 두 개 있다. 어떻게 하면 좀 더 적게 던져서 유리구슬의 강도를 알아낼 수 있을까?!
#(참고사항) 문제의 취지 : break구문, 진수표현
'''

#입력 : 구슬 개수. 건물 층수. 구슬이 처음으로 깨지는 층수(or 깨지지 않는 마지막 층수)
#출력 : 검사 횟수(=구슬을 던진 횟수)

#f = int(input('몇 층 건물인지 입력해주세요 :'))
#gb = int(input('몇 개의 구슬인지 입력해주세요 :'))
#key = int(input('구슬의 강도(깨지지 않는 마지막 층수) : '))

#def 깨진다 안깨진다 함수??(): 반환값은 bool

def next_check_floar(f, gb, count): #남은 층수에서 다음 검사할 위치를 찾아주는 함수
    
    if gb == 0:
        print('[{:3}] next check floar :{:3}'.format(count,0), end=', ')
        next_check_floar = 0
    elif gb == 1:
        print('[{:3}] next check floar :{:3}'.format(count,1), end=', ')
        next_check_floar = 1
    elif gb == 2: #x가 0인 경우 수행 문장 쓸 것.
        for i in range(f): #sqrt함수의 소스코드를 보는 방법이 없을까
            if i**2 <= f < (i+1)**2:
                print('[{:3}] next check floar :{:3}'.format(count,i), end=', ')
                next_check_floar = i
    else: #구슬이 3개 이상
        print('[{:3}] next check floar :{:3}'.format(count,f//2), end=', ')
        next_check_floar = f // 2
    
    return next_check_floar

def strength_of_glass_bead(f,gb,key): #유리구슬의 단단한 정도를 알려주는 함수
    
    count = 1
    while 1:
        n = next_check_floar(f,gb,count)
        # n 수정 필요.
        if n > key: # 구슬이 깨질 때
            gb -= 1
            f = n
            print('bead is broke!, bead : {:3}, remaining floaor : {:3}, key : {:3}, current floar : {:3}'.format(gb, f, key, 0))
        elif n < key: #구슬이 안깨질 때
            f -= n
            key -= n
            print('bead is ok!,    bead : {:3}, remaining floaor : {:3}, key : {:3}, current floar : {:3}'.format(gb, f, key, 0))
        else: # n == key
            print('this is key!,   bead : {:3}, remaining floaor : {:3}, key : {:3}, current floar : {:3}'.format(gb, f, key, 0))
            break
        
        
        count += 1

    print('count :', count)
    return count

        #if f == 0 or f == : 
        #    break
  
print('\n:)\n')

f = 100
gb = 2
key = 100
r = 0 #구슬을 던진 횟수
print('builing floar : {:3}, key floar : {:3}, bead : {:3}'.format(f,key,gb))      
strength_of_glass_bead(f,gb,key)

#꼭대기층 == key 일때 에러메세지 해결
#3, 10층 건물의 다음 탐색 알고리즘 확인. -> 현재는 1**2 <= 3 <2**2 에서 n=1, 2**2 <= 8 < 3**2 에서 n=2 이다. 8 = 2*4 +  