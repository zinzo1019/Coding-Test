# 보드판 크기 입력받기
n = int(input())

# 출발
x, y = 1, 1

# 명령 입력받기
directions = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 위치 임시 저장
nx, ny = 0, 0

for dir in directions:
    for i in range(len(move_types)):
        if dir == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny

print(x, y)
