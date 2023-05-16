# 시각 입력받기
n = int(input())
# 총 개수
total = 0

for hour in range(n+1):
    for minute in range(60):
        for second in range(60):
            if '3' in str(hour) + str(minute) + str(second):
                total += 1

print(total)
