import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
# 노드의 시작 번호 입력받기
start = int(input())

# 노드 정보를 담을 그래프 만들기
graph = [[] for _ in range(n+1)]
# 최단 거리를 모두 무한으로 초기화
distance = [INF] * (n+1)

# 노드와 간선 정보 입력받기
for _ in range(m):
    node1, node2, dis = map(int, input().split())
    graph[node1].append((node2, dis))

def dijkstra(start):
    # 방문할 노드를 우선순위 큐로 관리
    q = []
    # 시작 노드와 시작 노드 사이 거리는 0
    distance[start] = 0
    # 우선순위 큐에 시작 노드를 담고 시작
    heapq.heappush(q, (0, start))

    # 더이상 방문할 노드가 없을 때까지 반복
    while q:
        # 방문할 노드를 가져오되, 이미 방문한 노드는 제외
        dist, now = heapq.heappop(q)
        # 방문할 노드
        if distance[now] < dist:
            continue
        # 방문할 노드와 연관된 노드 정보 가져오기
        for node in graph[now]:
            # node[0]은 인덱스, node[1]은 거리
            # cost = 현재 노드까지의 최단 거리 + 새 노드로의 이동 거리
            cost = dist + node[1]
            # 만약 현재 노드를 경유해서 가는 방법이 기존 방법보다 더 최단 거리라면
            if cost < distance[node[0]]:
                # 최단 거리 업데이트
                distance[node[0]] = cost
                # 우선순위 큐에 연관 노드와 (예상) 최단 거리 삽입
                heapq.heappush(q, (cost, node[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])