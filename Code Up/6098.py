# 11 * 11 개미 판 만들기
board = []
for i in range(11):
    board.append([])
    for j in range(11):
        board[i].append(0)

# 개미 판 입력받기
for i in range(10):
    array = input().split()
    for j in range(10):
        board[i + 1][j + 1] = int(array[j])

# 개미의 시작점이자 위치 (x는 세로. y는 가로)
x = 2; y = 2;

# 먹이를 찾아 움직이는 개미
while x < 10 and y < 10: # 개미 판을 넘어가기 전까지 반복
    board[x][y] = 9 # 시작
    if board[x][y+1] == 1: # 오른쪽으로 이동할 때 벽을 만난다면
        if board[x+1][y] == 1: # 아래로 이동할 때 벽을 만난다면
            break # 반복 탈출
        else: # 아래로 이동할 수 있다면
            x += 1 # 아래로 한 칸 내려가는데
            if board[x][y] == 2: # 먹이를 발견했다면
                board[x][y] = 9; # 그 위치를 9로 바꾸고
                break # 반복 탈출
    else: # 오른쪽으로 이동할 수 있다면
        y += 1 # 오른쪽으로 한 칸 이동했는데
        if board[x][y] == 2:  # 먹이를 발견했다면
            board[x][y] = 9 # 그 위치를 9로 바꾸고
            break # 반복 탈출

# 개미 판 출력
for i in range(1, 11):
    for j in range(1, 11):
        print(board[i][j], end=' ')
    print()