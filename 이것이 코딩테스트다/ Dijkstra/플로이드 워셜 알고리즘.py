"""
모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우
2차원 리스트에 최단 거리 정보 저장
"""

INF = int(1e9)

# 노드의 개수, 간선의 개수 입력받기
n = int(input())
m = int(input())

# 노드 정보를 담을 그래프 만들기
graph = [[INF] * (n+1) for _ in range(n+1)]

# 노드와 간선 정보 입력받기
for _ in range(m):
    node1, node2, dis = map(int, input().split())
    graph[node1][node2] = dis

# 본인 노드에서 본인 노드로 가는 길은 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n+1):
    print()
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')