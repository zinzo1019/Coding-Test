# 보드판 크기 입력받기
n = int(input())

# 빙향 입력받기
dir = list(map(str, input().split()))

# x축, y축 방향 설정 (순서대로 LRUD)
dir_x = [-1, +1, 0, 0]
dir_y = [0, 0, -1, +1]

# 현재 위치
x, y = 1, 1

def move(d, x, y):
    if d == 'L':
        x += dir_x[0]
        y += dir_y[0]
    elif d == 'R':
        x += dir_x[1]
        y += dir_y[1]
    elif d == 'U':
        x += dir_x[2]
        y += dir_y[2]
    elif d == 'D':
        x += dir_x[3]
        y += dir_y[3]
    # 현재 위치 반환
    return x, y

# 이동 시작
for d in dir:
    temp_x, temp_y = move(d, x, y)
    if (temp_x <= 0 or temp_x > 5) or (temp_y <= 0 or temp_y > 5):
        continue
    else:
        x = temp_x
        y = temp_y

# 출력
print(y, x)

