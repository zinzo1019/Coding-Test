# 막대 판 입력 받기
h, w = input().split()
w = int(w)
h = int(h)

# 막대 판 만들기
board = []
for i in range(h + 1):
    board.append([]) # [ {}, {}, {}, ... * (h+1)개 ]
    for j in range(w + 1):
        board[i].append(0) # [ {0, 0, 0, ... * (w+1)개}, ... * (h+1)개 ]

# 막대 정보 입력 받기
n = int(input())
for i in range(n):
    l, d, x, y = input().split()
    l = int(l); d = int(d); x = int(x); y = int(y);
    for j in range(l): # 막대의 길이만큼 반복
        if d == 1 and x <= h: # 세로 방향
            board[x][y] = 1
            x += 1
        if d == 0 and y <= w: # 가로 방향
            board[x][y] = 1
            y += 1

# 막대 판 출력
for i in range(1, h + 1):
    for j in range(1, w + 1):
        print(board[i][j], end=' ')
    print()

