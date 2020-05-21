#사전 A는 부서 A에 소속된 사람들의 이름과 생일이다
A = {'February':{13:['Cathy']}, 'May':{3:['Katie'], 8:['Peter', 'Bill']}}

'''
Cathy는 2월 13일생, Katie는 5월 3일생, Peter와 Bill은 5월 8일이
생일이라는 의미. 이 사전구조를 아래와 같이 바꾸시오.

{'Peter':['May', 8], 'Bill':['May',8], 'Katie':['May', 3], 'Cathy':['February', 13]}

그리고 새로 만든 사전을 이용해서 아래와 같이 출력되도록 하시오

Cathy's birthday : February/13
Katie's ...
'''

A2 = {}
for mon in A:
    for dat in A[mon]:
        nam_list = A[mon][dat]
        A2[nam_list[0]] = [mon, dat]
        if len(nam_list) > 1:
            A2[nam_list[1]] = [mon, dat]
for x,y in A2.items():
    print('{}\'s birthday : {}/{}'.format(x, y[0], y[1]))
