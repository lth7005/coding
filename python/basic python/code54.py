#population.txt.에 국가,인구,면적. 인구밀도는 인구수/면적.
#인구밀도 오름차순 출력
#결과는 1. Canada          3.70 ...

'''
>>>import operator
>>>D={'c':3, 'b':2, 'd':4, 'a':1}
>>>sorted_D=sorted(D.items(),key=operator.itemgetter(1))
>>>sorted_D
[('a',1),('b',2),('c',3),('d',4)]
'''
def popu_dens(x):
    for line in x:
        line_list=line.strip().split() #1번
        key,value=line_list[0],int(line_list[1])/int(line_list[2]) #2번
        popu_dict[key]=value #3번
    return popu_dict

def popu_sort(x):
    import operator
    sorted_x=sorted(x.items(),key=operator.itemgetter(1))
    return sorted_x
    

#main
f=open('54_population.txt','r')
popu_dict={}
popu_dict=popu_dens(f)
f.close()
popu_list_tupl=popu_sort(popu_dict)

i=1
for nat,dens in popu_list_tupl:
    print('{:>2}. {:<15}{:>10.2f}'.format(i,nat,dens))
    i+=1    #4번

#2번에서 int()를 빼먹음.
#1,2,3번을 줄여서 아래처럼 쓸 수 있음
#nati,popu,land=line.strip().split()
#popu_dict[nati]=int(popu)/int(land)
#4번 빼먹음
