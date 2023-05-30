import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
# 노드의 시작 번호 입력받기
start = int(input())

# 노드 정보를 담을 그래프 만들기
graph = [[] for _ in range(n+1)]
# 방문한 적이 있는지 체크하는 리스트
visited = [False] * (n+1)
# 최단 거리를 모두 무한으로 초기화
distance = [INF] * (n+1)

# 노드와 간선 정보 입력받기
for _ in range(m):
    node1, node2, dis = map(int, input().split())
    graph[node1].append((node2, dis))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
# 반환된 노드를 기준으로 연결된 노드를 재탐색해야 하기 때문
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

# 다익스트라 알고리즘
def dijkstra(start):
    # 시작 노드와 시작 노드 사이 거리는 0
    distance[start] = 0
    # 시작 노드와 연결된 노드와의 거리로 distance[] 초기화
    for node in graph[start]:
        distance[node[0]] = node[1]

    # 시작 노드를 제외한 (n-1)개의 노드에 대해서
    # 탐색하며 최단 경로를 업데이트 해야 하기 때문에 아래 과정을 (n-1)번 반복
    for i in range(n):
        # 방문하지 않았으며, 시작 노드에서 경로가 가장 짧은 노드 선택
        now = get_smallest_node()
        visited[now] = True
        # 선택 노드 기준으로 연결된 노드의 최단 거리를 탐색
        for node in graph[now]:
            # node[0] 노드까지 선택 노드를 경유해서 가는 최단 거리
            cost = distance[now] + node[1]
            # 경유해서 가는 방법이 최단 거리라면
            if cost < distance[node[0]]:
                # 거리 저장 배열을 수정
                distance[node[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
