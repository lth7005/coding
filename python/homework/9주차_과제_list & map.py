#9주차 과제

'''
사용자로부터 5개의 수를 입력받은 후
입력된 값들의 합, 평균, 최대값, 최소값을 출력하시오

단1, sum(), min(), max(), sum()/len()을 사용할 것
단2,아래 코드를 응용할 것
a,b,c,d,e = map(int, input('숫자 5개를 입력하세요: (ex:1 2 3 4 5):').split())
print(a,b,c,d,e)
'''

list_num = list(map(int, input('숫자 5개를 입력하세요: (ex:1 2 3 4 5):').split())) #map을 사용
#print(list_num)

#list_num = [int(input('%d번째 숫자를 입력하세요 :' %(i+1))) for i in range(5)] #list comprehension을 사용
#print(list_num)

print('합 :', sum(list_num))
print('평균 :', sum(list_num)/len(list_num))
print('최댓값 :', max(list_num))
print('최솟값 :', min(list_num))
