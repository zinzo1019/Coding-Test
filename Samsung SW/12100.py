# 보드의 크기 N * N
N = int(input())

# 보드 판
board = []

# 보드 판 입력받기
for i in range(N):
    b = list(map(int, input().split()))
    board.append(b)

# 좌우 블록 사이 빈칸 제거
def remove_left_zero():
    for i in range(N):
        count_zero = board[i].count(0) # 보드 판 빈칸(0) 개수
        if count_zero: # 빈칸(0)이 존재한다면
            for j in range(count_zero):
                board[i].remove(0) # 보드 판 빈칸(0) 제거 (한 쪽으로 모으기)
                board[i].append(0) # 배열 끝에 빈칸(0)

# 상하 블록 사이 빈칸 제거
def remove_up_zero():
    for i in range(N):
        for j in range(N):
            if board[j][i] != 0 and j < N-1: # 상하 기준으로 빈칸(0)을 발견하면
                board[j][i] = board[j+1][i] # 한 칸 위로 땡기기

# 왼쪽으로 합치기
def left_merge():
    # 블록 사이 빈칸 제거
    remove_left_zero()
    for i in range(N):
        for j in range(0, N, 2):
            if board[i][j] == 0: # 빈칸(0)을 만나면 반복 종료
                 break
            if j == (N-1): # 보드 판의 끝에 다달아 다음 블록과 비교할 수 없다면
                continue
            if board[i][j] == board[i][j+1]: # 맞닿은 두 블록의 크기가 같다면
                board[i][j] *= 2 # 숫자가 합쳐짐
                board[i][j+1] = 0 # 합침 당한 블록은 빈칸(0) 처리
    # 블록 사이 빈칸 제거
    remove_left_zero()

# 위로 합치기
def up_merge():
    # 블록 사이 빈칸 제거
    remove_up_zero()
    for i in range(N):
        for j in range(0, N, 2):
            if board[j][i] == 0: # 빈칸(0)을 만나면 반복 종료
                 break
            if j == (N-1): # 보드 판의 끝에 다달아 다음 블록과 비교할 수 없다면
                continue
            if board[j][i] == board[j+1][i]: # 맞닿은 두 블록의 크기가 같다면
                board[j][i] *= 2 # 숫자가 합쳐짐
                board[j+1][i] = 0 # 합침 당한 블록은 빈칸(0) 처리
    # 블록 사이 빈칸 제거
    remove_up_zero()


print('좌우 머지')
left_merge()
for i in range(N):
    for j in range(N):
        print(board[i][j], end=' ')
    print()

print('상하 머지')
up_merge()
for i in range(N):
    for j in range(N):
        print(board[i][j], end=' ')
    print()