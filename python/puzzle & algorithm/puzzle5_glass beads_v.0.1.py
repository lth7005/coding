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

'''
추가할 것 및 궁금한 것

#파이썬 내장함수의 소스코드 보는 방법은??
#현재 위치한 실제 층수를 출력하기
#진수 변환 코드로 다시 작성하기
'''

def NextCheckFloar(f, gb, count): #남은 층수에서 다음 검사할 위치를 찾아주는 함수
    if gb in {0,1}: #구슬이 1개 (또는 0개?)
        print('[{:3}] next check floar :{:3}'.format(count,gb), end=', ')
        next_f = gb
    elif gb == 2: #구슬이 2개
        for i in range(1,f+1):
            if f // i in [i-1, i]:
                next_f = i
                print('[{:3}] next check floar :{:3}'.format(count,i), end=', ')
    else: #구슬이 3개 이상
        print('[{:3}] next check floar :{:3}'.format(count,f//2), end=', ')
        if f // 2: # 몫이 0이 아닌 경우
            next_f = f // 2
        else: # 몫이 0인 경우, 위의 if문에서 몫이 0이고 next_f = 0 하면 무한루프 발생
            next_f = 1
    
    return next_f

def HowManyThrowGlassBeads(f,gb,key): #단단한 정도를 알아내는 데 구슬을 던진 총 횟수를 반환
    count = 1
    while 1:
        n = NextCheckFloar(f,gb,count)
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

#main
print('\n:)\n')

lst = input('건물의 층수, 구슬의 개수, 구슬이 깨지지 않는 마지막 층수 :').split(',')
f = int(lst[0]) #건물의 층수
gb = int(lst[1]) #구슬의 개수
key = int(lst[2]) #구슬의 강도(구슬이 깨지지 않는 마지막 층수)

print('builing floar : {:3}, key floar : {:3}, bead : {:3}'.format(f,key,gb))      
count = HowManyThrowGlassBeads(f,gb,key)

'''
#해설 본 후 추가 설명 : 
문제의 취지는 진수 변환이다.
문제의 포인트는 검사 횟수를 최소화하는 것이 아니라,
검사 횟수를 최소화해주는 '일정한 간격'은 얼마인가 이다.
해설 -> "n층과 구슬 d개가 주어졌을 때, r**d > n 인 r을 선택합니다. 
(중략) 우리는 자릿수가 d인 r진수의 숫자를 표현하고자 합니다."
'''

