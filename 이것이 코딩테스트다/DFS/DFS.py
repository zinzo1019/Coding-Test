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

# 방문 여부를 기록할 배열
# 모두 방문하지 않은 것으로 초기화
visited = [False] * 9

def dfs(graph, v, visited):
    # 노드 v 방문 처리
    visited[v] = True
    # 출력
    print(v, end=' ')
    # 노드 v에 연결된 노드들을 스택에 담는 것과 같은 효과
    for i in graph[v]:
        # 아직 방문하지 않았다면
        if not visited[i]:
            # 방문하지 않은 노드를 기준으로 다시 순회
            dfs(graph, i, visited)

dfs(graph, 1, visited)