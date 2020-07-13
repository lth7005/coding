
def Togm(stars):
    time_m=[[0,j] for j in range(1,13)]
    for in_t, out_t in stars:
        for i in range(1,13):
            if in_t <= i < out_t: time_m[i-1][0]+=1
    time_m_s=sorted(time_m)
    return time_m_s[-1][1], time_m_s[-1][0]
    
if __name__ == '__main__':
    stars = [(6,8), (6,12), (6,7), (7,8),
             (7,10), (8,9), (8,10), (9,12),
             (9,10), (10,11), (10,12), (11,12)]
    good_time=Togm(stars)
    print('Best time to attend the party is at {} o\'clock : {} celcbrities'
          .format(good_time[0],good_time[1]))

