'''동전 coin, 지갑 purse 두 개의 클래스 만들기
코인 : 동전 이름, 동전 가격 을 저장, 500, 100, 50, 10 4개의 객체 만들기
지갑 : 데이터 속성으로 코인 객체를 저장한 리스트를 갖음. 즉, 지갑 안에
        있는 동전 정보.
'''

class Coin:
    """동전 클래스는 하나의 동전을 표현하는 클래스
        동전의 이름과 가치를 데이터 속성으로 함"""


class Purse:
    """현재 지갑에 돈이 얼마 있는지를 저장하는 클래스
        데이터 속성으로 리스트를 갖음, 리스트에는 동전들이 저장"""


#main

c500=Coin('500원',500)
c100=Coin('100원', 100)
c50=Coin('50원',50)
c10=Coin('10원',10)

coins=[c500,c500,c100,c50,c500,c100,c500,c10,c50,c10]
my_purse=Purse(coins)
my_purse.add_coin(c100)
my_purse.add_coin(c50)

print('Total in my purse : {}'.format(my_purse.getTotal()))

#결과는 Total in my purse : 2470
