# 시작 위차 입력받기
start = input()
# 경우의 수
total = 0

# LRUD L자 이동 ex) 왼왼아래, 왼왼위, 오오아래,...
dx = [-2, -2, +2, +2, +1, -1, +1, -1]
dy = [+1, -1, +1, -1, -2, -2, +2, +2]

# 문자 -> 정수 변환 ex) a -> 1, b -> 2, ...
x = ord(start[0]) - 96
y = int(start[1])

for i in range(8):
    # 총 8가지의 L자 이동 반복
    nx = x + dx[i]
    ny = y + dy[i]

    # 8 * 8 판을 벗어났을 경우 개수를 세지 않음
    if nx < 1 or nx > 8 or ny <1 or ny > 8:
        continue
    else:
        total += 1

print(total)