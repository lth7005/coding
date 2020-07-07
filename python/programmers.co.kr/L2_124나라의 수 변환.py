#test2 코딩문제
'''
124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.
124 나라에는 자연수만 존재합니다.
124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.

10진법	124 나라	10진법	124 나라
1   	1	        6	    14
2	    2           7	    21
3	    4	        8	    22
4	    11          9	    24
5	    12	        10	    41

자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록 solution 함수를 완성해 주세요.

제한사항
n은 500,000,000이하의 자연수 입니다.

입출력 예
n	result
1	1
2	2
3	4
4	11
'''

# 1,2,4 -> 11,12,14 -> 21,22,24 -> ... 
# 124수는 3번 주기로 반복되는 수
# 3으로 나누어 떨어지는 10진수(3,6,9,...)를 124수로 표현하는 팁1 : 3의 배수 => 몫 -1, 나머지 +3
# 3으로 나누어 떨어지는 10진수(3,6,9,...)를 124수로 표현하는 팁2 : 18 = 3*6 = 3*(6-1) + 3 = 3*5+3 = 3*(3*1+2)+3 -> 18 = 124(124)
# 3으로 나누어 떨어지는 10진수(3,6,9,...)를 124수로 표현하는 팁2 : 9 = 3*3 = 3*(3-1) + 3 = 3*2 +3 -> 9 = 24(124) <-3을 4로 바꿈
'''
def solution(n):
    answer = ''
    return answer
'''

#아래 함수는 다음의 계산 과정을 함수로 표현한 것 
#45 = 3*15 = 3*14 +3 = 3*(3*4 +2) +3 = 3*(3*(3*1 +1) +2) +3
#몫 1, 나머지 1, 2, 3 따라서 십진수 45는 124나라의 수로 표현하면 1124

def solution(n): 

    list_124 = ['1','2','4']     #3으로 나눈 나머지를 이 리스트의 인덱스 번호로 사용 -> answer += list124[나머지값-1]
    num_124 = ''    #3으로 나눈 나머지가 역순으로 저장됨. -> ex)십진수 45가 4211로 저장됨
    answer = ''     #역순으로 저장된 124나라 수를 다시 역순으로 저장할 변수

    quotient = n // 3   #quotient : 몫
    remainder = n % 3   #remainder : 나머지

    while 1:
        if remainder == 0:
            quotient -= 1
            remainder += 3
        num_124 += list_124[remainder-1]    #answer += '4' 도 가능
        #print('remainder to num_124')
        #print(quotient)
        #print(remainder)

        if quotient == 0:   #3으로 나눈 몫이 0인 경우는 1,2 뿐
            break
        elif quotient <= 3:
            num_124 += list_124[quotient-1]
            break
            #print('quotien <= 3')
            #print(quotient)
            #print(remainder)
        else:   #몫이 3보다 큰 경우
            remainder = quotient % 3
            quotient = quotient // 3
            #remainder = quotient % 3  ---> 몫이 바로 위의 식 때문에 바뀌어버렸다. 이 식을 위에 써야함.
            #print('quotient > 3')
            #print(quotient)
            #print(remainder)

    for i in range(1,len(num_124)+1):   #역순으로 저장된 124나라 수를 다시 역순으로 저장
        answer += num_124[-i]

    return answer

#main
num = int(input('enter number to \'124\':'))
print('number {} of 124 : {}'.format(num, solution(num)))