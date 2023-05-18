# 얼음판 크기 입력받기
n, m = map(int, input().split())

# 얼음판 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 얼음 개수
count = 0

# 동서남북
dx = [+1, -1, 0, 0]
dy = [0, 0, +1, -1]

# 새로운 얼음 덩어리를 탐색하면 True가 반환됨
# 새로운 얼음 덩어리를 탐색하지 못하면 False가 반환됨
def dfs(x, y):
    # 얼음판을 벗어나면 바로 종료
    if x <= -1 or x >= n or y < 0 or y >= m:
        return False

    # 만약 아직 방문하지 않은 얼음이라면
    if graph[x][y] == 0:
        # 방문 처리
        graph[x][y] = 1
        # 동서남북 4가지 방향으로 재탐색
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        # 얼음 탐색을 마치면 True 반환
        return True

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1

print(count)