"""
1번부터 n번까지의 회사가 있는데 특정 회사끼리는 서로 도로를 통해 연결되어 있다.
판매원 A는 현재 1번 회사에 위치해 있으며, X번 회사에 방문해 물건을 판매하고자 한다.
연결된 두 개의 회사는 양방향으로 이동할 수 있다.
또한 오늘 판매원 A는 X번 회사에 방문하기 전에 K번 회사에 찾아가 소개팅을 할 예정이다.
판매원이 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성하시오.
"""

INF = int(1e9)

# 회사의 개수 n과 경로의 개수 m 입력받기
n, m = map(int, input().split())

# 경로 입력받기
graph = [[] for i in range(n+1)]
for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

# 최종 회사 x와 소개팅 장소 k 입력받기
x, k = map(int, input().split())


# 다익스트라 알고리즘
def dijkstra(start):

    # 최단 경로를 저장하는 배열
    distance = [INF] * (n + 1)
    distance[start] = 0
    # 방문 여부를 저장하는 배열
    visitied = [False] * (n + 1)

    # 큐 선언
    queue = []
    # 시작 노드 방문 처리
    visitied[start] = True
    for node in graph[start]:
        distance[node] = 1
        queue.append(node)

    while queue:
        # 현재 위치 갱신
        now = queue.pop()
        # 방문한 노드라면 건너뛰기
        if visitied[now]:
            continue
        # 기존의 방법과 now 노드를 경유하는 방법 중 더 짧은 방법을 선택해서 distance[] 배열에 업데이트
        for node in graph[now]:
            if distance[node] > (distance[now] + 1):
                distance[node] = distance[now] + 1
                queue.append(node)

    return distance

result = dijkstra(1)[k] + dijkstra(k)[x]
if result >= INF:
    print(-1)
else:
    print(result)
