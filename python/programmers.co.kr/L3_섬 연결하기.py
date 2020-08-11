#섬의 개수 n은 1 이상 100 이하
#costs의 길이는 len(costs) <= ((n-1)*n) / 2 이하 -->  'costs의 길이' = 간선의 수

'''
코딩 과정
1.비용 정렬
2.
3.방문 노드 체크
'''


def solution(n, costs): #크루스칼 알고리즘
    answer = 0
    
    #비용 정렬하기
    for i in range(len(costs)):
        costs[i].reverse()
    costs.sort()
    print(costs)
    
    #닫힌 노드(사이클 발생) 판단하기 -> 이걸 어떻게 해야하나...
    #
    
    nodes = list() # nodes = [[a,b],...] 에서 a는 노드 번호, b는 노드의 접점 개수
    for i in range(len(costs)):
        nodes.append(costs[1:3])
        
        
        pass      
    
    return answer


print(':)')


#costs = input('enter costs :')
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
n = 4

solution(n,costs)
