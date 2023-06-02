"""
n개의 집과 m개의 길로 이루어진 마을이 있다.
길은 양방향이며 그 길을 유지하는 데 드는 유지비가 있다.
마을의 이장은 마을을 2개의 분리된 마을로 분할할 계획을 세우고 있다.
각 분리된마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야 한다.
필요없는 길은 없애고 유지비의 합을 최소로 하는 프로그램을 작성하시오.
"""
import heapq

# 집의 개수 n과 길의 개수 m 입력받기
n, m = map(int, input().split())


# 우선순위 큐로 사용할 배열
queue = []

# 길 입력받기
graph = [[] for _ in range(n+1)]
for _ in range(m):
    n1, n2, cost = map(int, input().split())
    # 우선순위 큐에 삽입
    heapq.heappush(queue, (cost, n1, n2))

# 부모 노드를 저장하는 배열 & 초기화
parent = []
for i in range(n+1):
    parent.append(i)

# 최상위 부모 노드를 찾는 함수
def find_top(n):
    if n != parent[n]:
        parent[n] = find_top(parent[n])
    return n

# 합치기 함수
def union(n1, n2):
    p_n1 = find_top(n1)
    p_n2 = find_top(n2)
    if p_n1 < p_n2:
        parent[p_n2] = p_n1
    else:
        parent[p_n1] = p_n2

# 크루스칼 알고리즘
def kruskal():
    # 총 유지비
    result = 0
    # 간선의 개수
    road = 0

    # 마을을 두 개로 나누어야 하므로
    # 간선의 개수가 (n-2)개가 될 때까지만 반복
    while queue and road < n-2:
        # 간선의 개수 + 1
        road += 1
        # 우선순위 큐에서 정보 가져오기
        cost, n1, n2 = heapq.heappop(queue)

        # 사이클 판별
        if find_top(n1) != find_top(n2):
            union(n1, n2)
            result += cost

    return result

print(kruskal())