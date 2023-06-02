from collections import deque

# 노드와 간선 개수 입력받기
v, e = map(int, input().split())

# 차수 저장 배열
indegree = [0] * (v+1)

# 그래프 정보 입력받기
graph = [[] for _ in range(v+1)]
for i in range(e):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    indegree[n2] += 1

# 결과를 담을 배열
result = []

# 큐 생성
queue = deque()

# 차수가 0이라면 큐에 삽입
for n in range(1, v+1):
    if indegree[n] == 0:
        queue.append(n)

# 큐가 빌 때까지 반복
while queue:
    # 현재 노드
    now = queue.popleft()
    # 결과에 추가
    result.append(now)
    # 현재 노드와 연결된 간선 제거
    for n in graph[now]:
        indegree[n] -= 1
        # 만약 차수가 0이 됐다면
        if indegree[n] == 0:
            # 큐에 삽입
            queue.append(n)

# 출력
for r in result:
    print(r, end=' ')