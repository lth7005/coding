#특정 시간 a부터 b까지-[a,b) 주어진다면 그 시간 동안 만나는 사람 최대 수 구하기

def Togm(stars,me_in,me_out):
    time_m=[[0,j] for j in range(1,13)]
    for in_t, out_t in stars:
        if me_in>=out_t or me_out<=in_t: pass
        else:
            for i in range(me_in,me_out):
                if in_t <= i < out_t: time_m[i-1][0]+=1
    #print(time_m) 확인용
    return sorted(time_m)[-1]
    
if __name__ == '__main__':
    
    stars = [(6,8), (6,12), (6,7), (7,8),
             (7,10), (8,9), (8,10), (9,12),
             (9,10), (10,11), (10,12), (11,12)]
    
    a,b = input('Enter your time : ').split()
    me_in=int(a) #my_time = int(a), int(b) 로 바꿔보기
    me_out=int(b)
    
    celeb, oclock = Togm(stars,me_in,me_out)
    print('Best time to attend the party is at {} o\'clock : {} celcbrities'
          .format(oclock,celeb))

