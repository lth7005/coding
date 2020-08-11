
'''
이진 트리와 순회 요약, '인공지능을 위한 이산수학' - 최종명 교수님(저)
이진 트리 - 프림 알고리즘(또는 크루스칼 알고리즘)으로 최소신장트리를 종이에 써본다.
종이에 그린 트리를 프로그램으로 구현하기 위해서는 '링크드 리스트'라는 자료구조로 이 트리의 노드를 표현해야한다.
한편, 전위 중위 후위 순회는 이진 트리를 순회하는 3가지 방법을 말하며,
순회란 이진(? 그냥 트리? 이진트리?) 트리의 모든 노드를 방문하는 것을 말한다.
이진 트리 내의 모든 노드들을 순회하면, 방문하는 순서에 의해서 각 노드들에 대한 선형(직선의 형태?)적인 순서가 만들어진다.
'''

class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.left = left
        self.right = right

    '''
    스페이스바 4칸으로 들여쓰기 되어있는 이 주석을  "<---" 왼쪽으로 딱 붙이면
    에러 발생
    def preorder(self, answer):
    ^
    IndentationError: unexpected indent
    '''
    '''
    아래를 참고해서, 위의 def __init__()에 빠진 주석(궁금한 것, 생각의 흐름 등) 추가해서 넣기 
    class Node:  
        def __init__(self, value, left=None, right=None):  
            #add(3) 이라고 하면, 자동으로 3은 이 __init__() 함수에 적용되는 걸까?
            #그래서 3이 이 클래스의 속성(attribute)으로 정해진다? add(3)만 해도?
            #아니면, 반드시 Node(3)이라고 해야 3을 이 Node 클래스의 속성으로 설정할 수 있는 걸까?
            self.value = value  
            # Node(5)하고 add(3)하면, 
            # add()함수 안에서 'self.value' 는 5다? 3이다? 
            self.left = left
            self.right = right
    '''

    def preorder(self, answer):  #전위 순회 #self만 있는 건 무슨 뜻일까?
        print(self.value, end=' ')
        answer.append(self.value)
        if self.left != None:
            self.left.preorder(answer)
        if self.right != None:
            self.right.preorder(answer)
        
        return answer

    '''
    def preorder(self):  #전위 순회
    print(chr(self.value))
    if self.left != None:
        self.left.preorder()
    if self.right != None:
        self.right.preorder()
    반환값 없이 곧바로 출력할 수도!
    '''
    
    def inorder(self, answer):  #중위 순회
        if self.left != None:
            self.left.inorder(answer)
        print(self.value, end=' ')
        answer.append(self.value)
        if self.right != None:
            self.right.inorder(answer)
            
        return answer
            
    def add(self, value):    #'링크드 리스트' 자료구조를 구현한 코드
        #링크드 리스트 : 각 노드가 데이터와 포인터를 가지고 한 줄로 연결되어있는 방식으로 데이터를 저장하는 자로구조 (위키백과)
        #한 줄로 연결됐다? 그렇다면 이 구조에서 각 노드는 오직 하나의 자식(우측 또는 좌측)만 갖는다?
        if self.value == value:
            return
        
        if self.value > value:   # a.add(b) 라고 호출한다면 self.value 가 a 이고 value 가 b 이다.
            # a.add(b) 에서 b처럼, 추가시킬 데이터값(b, value)가 현재의 노드(a, self.value)보다 작을 때
            # 잠깐, 부모노드 : a, self.value / 자식노드 : self.left(or right) / 자식노드에 추가할 데이터 : b / 아닌가?
            # 이것 역시 객체와 주소. 그러니까 'left, date, right' 라는 자료구조를 정확하게 알아야 이해가 될 것 같다. 
            # 이 left, right는 'id(변수)'처럼 메모리 주소를 뜻하는 것 같은데...
            if self.left == None:   # 그리고 부모노드(a, self.value)의 왼쪽 자식노드(self.left)가 NULL일 때
                self.left = Node(value)  # 부모노드의 왼쪽 자식노드(self.left)에 데이터값(b,value)를 Node라는 클래스 속성으로 저장한다.
                # self.left = value 라고 해버리면? -> Node(data) 는 data에 Node라는 클래스의 left와 right 속성을 부여해서 
                # 하나의 노드를 '링크드 리스트' 형태로 만들어준다 -> 'left, data, right' 가 하나의 노드.
                # 그리고 이 left와 right는 특별한 말이 없으면,
                # Node클래스의 속성을 정의하는 __init__() 매개변수에서 None으로 초기화했듯이,
                # default값인 NULL, None으로 초기화 된다.  
                # 그냥 value로 해버리면? data에 left, right라는 방향, 공간 자체가 없어서 data만...?
            else:  # 부모노드의 왼쪽 자식노드에 값이 있으면(=NULL이 아니면)
                self.left.add(value)   # 주의! 혼동하기 쉬운. 이 add()함수의 가장 핵심적인 부분
                # 'self.left' 라는 객체가 add() 함수를 호출했다.
                # 그래서 이곳에서 호출한 add() 함수 안의 self는 'self.left' 에 해당한다.
                # 즉, (self.left).left로 진행되는 것. 그리고 이것이 반복되서 또 add()함수를 만나면
                # ((self.left).left).left 처럼 진행된다. 자식 노드의 자식노드의 자식노드.   
                # 자신이 자신을 호출했다. 그리고 또 호출한다. 호출과 호출 사이에서 어떤 일을 하면서.
                
        else:  # 추가시킬 데이터값(b, value)이 현재의 노드(a, self.value)보다 클 때
            if self.right == None: #그리고 현재의 노드(self.value)의 우측 자식노드(self.right)가 NULL이면
                self.right = Node(value)
                # 이 우측 자식 노드(self.right)에 Node의 속성(left, right)이 추가된 데이터값을 넣는다.
                # '우측? 넣는다?' : b의 메모리주소 'id(b)' 를 self.right로 설정한다?!
            else:  # 부모노드의 왼쪽 자식노드에 값이 있으면(=NULL이 아니면)
                self.right.add(value)    # 위와 같은 의미
        #add()함수에서 데이터를 삽입하는 또는 search()에서 검색하는 간격이 '유리구슬 문제'의 간격??

    '''
    아래를 참고해서, 위의 def add()에 빠진 주석(궁금한 것, 생각의 흐름 등) 추가해서 넣기         
    def add(self, value):  
            #이하의 add() 함수 코드는, 파이썬의 자로구조 중 '링크드 리스트'라는 자료구조의 형식에 따라 구현된 코드이다?
            #링크드 리스트 : 각 노드가 데이터와 포인터를 가지고 한 줄로 연결되어있는 방식으로 데이터를 저장하는 자로구조 (위키백과)
            #한 줄로 연결됐다면, 이 구조에서 각 노드는 오직 하나의 자식(우측 또는 좌측)만 갖는다?
            if self.value == value:
                return
            
            if self.value > value:   # 5 > 3 (주의!! : 현재 여기서 self.value는 5다!!??)
                if self.left == None:   #  5의 왼쪽 자식노드 없음
                    self.left = Node(value)  # 여기서 self.left는 5의 좌측?
                    # add(3)에서 처럼 3을 받아왔다. 이 3은 value 이다.
                    # Node(3) 은, 3을 Node 클래스의 속성값으로 설정한다는 뜻
                    # self.left(좌측 자식노드) 에 이 속성값 3을 넣는다. 
                    # 즉, 루트 노드 5(self.value)의 좌측 자식노드(self.left)에 3이라는 Node클래스 속성(값,정수)을 넣는다.
                    #최종 : add(3) 하면 이곳에 도착하는데,
                    # Node(3) 이라고 했으니 "NULL, 3, NULL" 이라는 형태의 데이터가 "TRUE, 5, NULL" 이라는 형태의 데이터 좌측에 저장된다. 
                    # 즉, 5의 좌측에 3이 있는데 이 3을 Node(3)으로 했기 때문에, 'NULL, 3, NULL' 이 5의 좌측에 있다. 
                else:  #  5의 왼쪽 자식노드가 이미 값이 있다면
                    self.left.add(value)   # 중요한 부분! 재귀함수? 현재 이곳(3)에서 add()함수를 호출한다.
                    #1. self = 5
                    #2. self.left = 3
                    #3. self.left.add(x) 안의 self = 3
                    #4. 즉, ~~~.add() 이니까 add()함수 안에서 self는 ~~~~이라는 뜻. 그런데 지금 ~~~~인 것이 "self.left"라는 것. -> a의 b의 c의 d의 ... 같은. 
            else:  # add(x) 에서 받아온 x가 로트 노드보다 더 큰 경우 
                if self.right == None: #그리고 루트 노드(self.value)의 우측 자식노드(self.right)가 NULL이면
                    self.right = Node(value)
                    # 이 우측 자식 노드(self.right)에 Node(x) 를 넣는다. -> '우측? 노드? x를 넣는다?' x의 메모리주소(id(x))를 self.right로 설정한다?!
                    # Node(x) 는 x라는 '것'(인수? 매개변수?)을 Node라는 클래스의 속성(__init__)으로 선언? 명명? 설정? 한다는 뜻이다.
                else:  # 5의 우측 자식노드가 이미 값이 있다면
                    self.right.add(value)    # 중요한 부분! 재귀함수? 현재 이곳(?)에서 add()함수를 호출한다. 
    '''

    def search(self, value):
        if self.value == value:
            return self
        elif self.value > value:
            if self.left != None:
                return self.left.search(value)
            
        else:
            if self.right != None:
                return self.right.search(value)
            
    def remove(self, value):
        pass # 코드 작성 필요

print('\n:)\n')
            
#문자        ->  'A'   'B'  'C'  'D'  'E'
#아스키 코드  ->  65    66   67   68   69
values = [69,68,66,65] 
#A - B - [C] - E - D 구조를 위한 입력 규칙 : 
# 1.C(67)가 가장 먼저 들어간다.
# 2.A(65)보다 B(66)가 먼저 들어가야 한다.
# 3.D(68)보다 E(69)가 먼저 들어가야 한다. 그래서
#values = [69,68,66,65] #도 가능하다. 또 ...
#그런데 중위, 후위 순회에서도 결과가 똑같을 지는 모르겠다. 직접 실행해보자.
root = 67
tree = Node(root)

print('자료 저장 순서       :', root, end=' ')
for x in values:
    tree.add(x)
    print(x, end=' ')

print('\n자료 저장 순서 ASCII : ', chr(root), end='  ')
for x in values:
    tree.add(x)
    print(chr(x), end='  ')
    
print('\n\n전위 순회 순서       :', end=' ')
answer = list()
answer = tree.preorder(answer)

print('\n전위 순회 순서 ASCII :', end=' ')
for i in answer:
    print('{:>2}'.format(chr(i)), end=' ')
    
print('\n중위 순회 순서       :', end=' ')
answer = list()
answer = tree.inorder(answer)

print('\n중위 순회 순서 ASCII :', end=' ')
for i in answer:
    print('{:>2}'.format(chr(i)), end=' ')
    
v = 66
print('\n검색', chr(v), '             :', end=' ')
result = tree.search(v)
if result == None:
    print('트리는', chr(v), '값을 갖고 있지 않음')
else:
    print('트리는', chr(result.value), '값을 갖고 있음')
