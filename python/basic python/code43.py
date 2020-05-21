m = {}
m[1] = ['Alice', 'Tom', 'David', 'Peter']
m[2] = ['Alice', 'Cindy', 'David', 'Eve', 'Peter']
m[3] = ['Mary', 'Tom', 'Bob', 'David', 'Jenny', 'Paul', 'Cindy']
m[4] = ['Cindy', 'David', 'Jenny', 'Bob', 'Tom']
m[5] = ['Alice', 'David', 'Eve', 'Paul', 'Bob']
m[6] = ['Cindy', 'David', 'Alice', 'Mary', 'Bob', 'Tom', 'Peter', 'Jenny']
m[7] = ['Peter', 'David', 'Tom']

#사전을 이용해서 이름을 키로, 출석 날짜를 리스트로 모아서 값으로 저장하고 출력

stu = {}

for a in m: #키인 날짜를 하나씩 가져옴
    for b in m[a]: #가져온 날짜의 값인 이름 리스트에서 이름을 하나씩 가져옴
        if b not in stu: stu[b] = [] #가져온 이름을 키로, 값은 빈 리스트
        stu[b].append(a) #이름에 해당하는 날짜를 리스트에 추
for x,y in stu.items():
    print(x, ':', y)
