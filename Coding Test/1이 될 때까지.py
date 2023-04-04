n, k = map(int, input().split())

count = 0 # 수행 횟수

while n > 1:
    if n % k == 0: # 나누어떨어진다면
        n /= k # n을 k로 나누기
    else: # 나누어떨어지지 않는다면
        n -= 1
    count += 1

print(count)
