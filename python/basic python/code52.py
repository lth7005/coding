#결과는 201812345 : 85.00 ...
#학번과 그 학생의 성적 네 개. 가장 좋은 성적 세 개의 평균 구하는 프로그램
#평균은 소수점 둘째 자리까지

f=open('52_score.txt','r')
score={}
values_d=[]
for line in f:
    line=line.split()
    key,values=line[0],sorted(line[1:])[1:]
    for i in range(len(values)):
        values_d.append(int(values[i]))
    score[key]=values_d
    print('{} : {:0.2f}'.format(key,sum(values_d)/len(values_d)))
    
    
f.close()

'''결과가 틀리게 나옴. 어디가 틀렸는지 찾고 고칠 것.'''
