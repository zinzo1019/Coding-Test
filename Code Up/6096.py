location = [] #1차원 배열 생성

# 바둑판 모두 0으로 초기화
for i in range(0, 19): # 0부터 18까지 총 19
    location.append([]) # [[], [], [], ... * 19] 2차원 배열 생성
    for j in range(0, 20):
        location[i].append(0)

# 바둑판 입력받은 대로 수정정for i in range(0, 19):  # 0부터 18까지 총 19
    temp = input().split() # i번째 줄 공백 기준으로 숫자 배열 저장 ex) [0, 0, 0, ... * 19]
    for j in range(0, 19):
        location[i][j] = int(temp[j])

# 십자 뒤집기 하기 위해 좌표 입력받기
repeat = int(input())
for i in range(repeat):
    x, y = input().split() # 바둑판 상 x좌표와 y좌표
    x = int(x) - 1 # (1, 1)을 십자 뒤집기 하고 싶다 -> 배열 상으론 (0, 0)을 뒤집어야 함
    y = int(y) - 1
    # 가로 뒤집기
    for n in range(19):
        if location[x][n] == 0:
            location[x][n] = 1
        else:
            location[x][n] = 0
    # 세로 뒤집기
    for n in range(19):
        if location[n][y] == 0:
            location[n][y] = 1
        else:
            location[n][y] = 0

# 바둑판 출력
for i in range(19):
    for j in range(19):
        print(location[i][j], end=' ')
    print()

