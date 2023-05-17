from collections import deque

# 무방향 그래프 인접 리스트 표현
graph = [
    [], # 0번 노드는 존재하지 않음
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7] # 8번 노드
]

visited = [False] * 9

def bfs(graph, start, visited):
    # 시작 지점을 큐에 넣고 방문 처리
    queue = deque([start])
    visited[start] = True

    # 큐가 끝날 때까지 반복
    while queue:
        # 큐에서 하나 가져옴
        node = queue.popleft()
        print(node, end=' ')
        # 방문하지 않은 인접한 노드를 전부 큐에 담고 방문 처리
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)