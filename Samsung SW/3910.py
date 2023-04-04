# 보드 판의 길이
N = int(input())

# 보드 판 만들기 & 0으로 초기화
# 0행 0열은 코드상 존재할 뿐 버릴 예정
board = []
for i in range(0, N+1): # 0열부터 N열까지 총 (N+1)열
    board.append([])
    for j in range(0, N+1): # 0행부터 N행까지 총 (N+1)행
        board[i].append(0)

# 사과 개수와 위치
K = int(input())
for i in range(K):
    x, y = map(int, input().split()) # 사과의 좌표
    board[x][y] = 1 # 사과의 위치를 1로 표기

# 시계 방향으로 움직임 (동남서북)
dx = [+1, 0, -1, 0]
dy = [0, +1, 0, -1]

# dx[], dy[] 방향 배열의 인덱스 역할
# 첫 시작 방향은 동쪽이므로 0으로 설정
dir = 0

# 시간에 따른 명령
cmd = [0] * 10001
# 명령 입력받기 (초와 방향)
L = int(input())
for i in range(L):
    t, d = input().split()
    t = int(t)
    cmd[t] = d # t초에 명령 d

# max_time = int(cmd_temp[L-1][0]) # 가장 마지막 명령의 초가 뱀의 최대 이동 시간
# cmd = [0] * (max_time + 1)
# for i in range(L):
#     cmd[cmd_temp[i][0]] = cmd_temp[i][1] # 초에 따른 방향 저장

# 시작 시간
time = 0
# 시간에 따른 뱀의 머리의 위치를 저장할 배열 ex) 0초에는 (1, 1)에 위치함
snake_x, snake_y = [0], [0]

# 뱀의 현재 머리 위치 (1, 1)
head_x, head_y = 1, 1
snake_x[time] = 1
snake_y[time] = 1

# 뱀의 꼬리
# 뱀의 꼬리는 뱀의 머리가 움직인 위치를 그대로 따라갈 수밖에 없기에
# snake_x[]와 snake_y[]에서 인덱스 조절만 하면 꼬리의 위치를 알 수 있다.
# ex) 뱀의 머리가 snake_x[5], snake_y[5]에 위치하고
# ex) 뱀의 길이가 2일 때, 뱀의 꼬리의 위치는 snake_x[4], snake_y[4]이다.
tail_index = time

def print_board():
    for i in range(1, N+1):
        for j in range(1, N+1):
            print(board[i][j], end=' ')
        print()

# 게임 시작
while True: # 규칙을 위반하지 않는 한 계속 진행
    time += 1 # 시간이 1초씩 흘러감

    # 뱀의 머리 좌표는 시간에 따라 이동
    head_x += dx[dir]
    head_y += dy[dir]

    # 뱀의 머리가 보드를 벗어나거나 자신의 몸에 부딪히거나 명령이 끝나면 종료
    if (head_x < 1 or head_y < 1 or head_x > N
            or head_y > N or board[head_y][head_x] == -1):
        break

    # 뱀의 위치가 유효하다면
    # 배열에 뱀의 위치를 기록
    snake_x.append(head_x)
    snake_y.append(head_y)

    # 사과를 찾지 못했다면
    if board[head_y][head_x] == 0:
        # 뱀의 꼬리가 뱀의 머리를 따라가도록
        # 뱀의 꼬리가 있던 좌표의 값을 0으로 만듦
        board[snake_y[tail_index]][snake_x[tail_index]] = 0
        tail_index += 1

    # 뱀의 위치를 -1로 처리
    board[head_y][head_x] = -1

    # 방향 전환
    if cmd[time] == 'D':
        dir = (dir + 1) % 4
    if cmd[time] == 'L':
        dir = (dir + 3) % 4

    print("time is " + str(time))
    print_board()
    print()

print(time)
