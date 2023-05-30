"""
어떤 나라의 n개의 도시, 단방향 연결
도시 c에서 위급 상황 발생. 최대한 많은 도시로 메시지를 보내고자 한다.
각 도시의 번호와 통로가 설치되어 있는 정보가 주어질 때,
도시 c에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇 개이며 도시들이 모두 메시지를 받는 데까지 걸리는 시간은 얼마인가.
"""
INF = int(1e9)

# 도시의 개수 n, 통로의 개수 m, 메시지를 보내고자 하는 도시 c 입력받기
n, m, c = map(int, input().split())

# 통로에 대한 정보 입력받기
graph = [[] for _ in range(n+1)]

for i in range(m):
    start, end, dist = map(int, input().split())
    graph[start].append((end, dist))

# 시작 노드와 연결 노드 사이 거리로 distance[] 배열 초기화
distance = [[INF] * (n+1)] * (n+1)
for i in range(1, n+1):
    for j in graph[i]:
        distance[i][j[0]] = j[1]

for a in range(1, n+1):
    for b in range(1, n+1):
        for c in range(1, n+1):
            distance[b][c] = min(distance[b][c], distance[b][a] + distance[a][c])

#                         나라의 개수
count = 0
for i in range(0, n+1):
    if distance[c][i] >= INF:
        distance[c][i] = -1
    else:
        count += 1

# 모든 나라가 메시지를 받는 데 걸리는 시간
max_value = sorted(distance[c], reverse=True)[0]

print(count, max_value)