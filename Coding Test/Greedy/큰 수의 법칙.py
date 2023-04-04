N, M, K = map(int, input().split())

# 리스트 내림차순 정렬
list = list(map(int, input().split()))
list.sort()
list.reverse()

count = 0
total = 0

for i in range(M):
    if count == K:
        total += list[1]
        count = 0
    else:
        total += list[0]
        count += 1

print(total)