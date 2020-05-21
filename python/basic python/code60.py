class Friend:
    #친구 클래스, 데이터 속성으로 친구 이름, 친구 알게 된 나이.
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def getname(self):
        return self.name
    def getage(self):
        return self.age

#main
f1=Friend('Alice', 10)
f2=Friend('Paul', 13)
f3=Friend('Cindy', 17)
f4=Friend('David', 7)

friends=[f1,f2,f3,f4]

print('제일 오랜 친구 이름 :', end='')

#제일 오래된 친구 이름을 구하는 코드 작성
#name=friends.oldest_f_n()
oldest_age=100
for friend in friends:
    if  friend.getage() < oldest_age:
        age=friend.getage()
        name=friend.getname()

print(name)

#제일 오랜 친구 이름 :David
     
