#9주차 과제
#list comprehension을 이용해서 작성

'''
사용자로부터 5개의 수를 입력받은 후
입력된 값들의 합, 평균, 최대값, 최소값을 출력하시오
단, sum(), min(), max(), sum()/len()을 사용할 것
'''

list_str = input('5개의 수를 입력하세요:').split(' ')
#print(list_str) #확인용 print

list_int = [int(i) for i in list_str]
#print(list_int) #확인용 print

print('합 :', sum(list_int))
print('평균 :', sum(list_int)/len(list_int))
print('최댓값 :', max(list_int))
print('최솟값 :', min(list_int))


'''
#for문을 사용해서 작성

list_int2 = []
a = 0
for i in list_str:
    list_int2.append(int(list_str[a]))
    a+=1
#print(list_int2) #확인용 print

print('합 :', sum(list_int2))
print('평균 :', sum(list_int2)/len(list_int2))
print('최댓값 :', max(list_int2))
print('최솟값 :', min(list_int2))
'''
