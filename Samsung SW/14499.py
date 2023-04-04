dice = [] # 주사위
for i in range(6):
    dice.append(0) # 주사위 값은 0으로 초기화

# 세로 크기 / 가로 크기 / 주사위 좌표 / 명령 개수
N, M, x, y, K = input().split()
N = int(N); M = int(M); x = int(x); y = int(y);

board = [] # 주사위 판
# 주사위 판 입력받기 (정수형)
for i in range(int(N)): # 세로
    board.append([])
    array = input().split()
    for j in range(int(M)): # 가로
        board[i].append(int(array[j]))

# 명령 입력받기 (# 동 1 서 2 북 3 남 4)
direction = input().split()

# 주사위 이동 (동서북남)
def move(direction):
    if direction == 1:
        dice[1], dice[3], dice[4], dice[5] = dice[4], dice[5], dice[3], dice[1]
    elif direction == 2:
        dice[1], dice[3], dice[4], dice[5] = dice[5], dice[4], dice[1], dice[3]
    elif direction == 3:
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
    elif direction == 4:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]

# 주사위 판 <-> 주사위 복사하기
def copy_dice(x, y):
    if not board[x][y]: # 주사위 판의 값이 0이라면
        board[x][y] = dice[3] # 주사위 -> 주사위 판 복사
    else: # 주사위 판의 값이 0이 아니라면
        dice[3] = board[x][y]  # 주사위 판 -> 주사위 복사
        board[x][y] = 0 # 주사위 판의 값은 0으로 초기화

board_move = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)] # 동서북남
result = [] # 출력 값

for k in range(int(K)): # 명령 개수
    dir = int(direction[k])
    dx, dy = board_move[dir] # 방향에 따라 움직이는 x, y 좌표
    dx+=x # x 좌표 이동해서 dx에 저장
    dy+=y # y 좌표 이동해서 dy에 저장
    if 0<=dx<N and 0<=dy<M: # 주사위 판을 넘기지 않는다면
        move(dir) # 주사위 이동
        copy_dice(dx, dy) # 주사위 판 <-> 주사위 복사
        result.append(dice[1])
        x, y = dx, dy

for i in result:
    print(i)