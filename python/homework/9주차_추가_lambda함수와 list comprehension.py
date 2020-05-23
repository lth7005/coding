# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:05:33 2020

@author: lth7000
"""

#lambda 함수와 list comprehension

#1.lambda 함수, 람다함수는 이름없는 def 함수.
n = lambda x,y : x + y #x,y를 인수로 가져와서 더한 값을 반환하는 이 함수의 이름은 n
k=n(4,5) #이렇게 n이라고 이름을 붙여서 사용할 수도 있다.
print(k) 

#2.list comprehension, 
m = [x**2 for x in range(1,11) if x % 2 == 0] #1부터 10까지 짝수의 제곱을 차례로 리스트에 저장.
print(m)
