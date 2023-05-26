"""
n가지 종류의 화폐, 그 가치의 합 m
m을 만드는 화폐의 최소한의 개수를 구하라
"""

# n과 m 입력받기
n, m = map(int, input().split())

# 화폐 입력받기
moneys = []
for _ in range(n): moneys.append(int(input()))
moneys.sort()

# 가치 m을 만들기 위한 최소한의 화폐 개수를 저장하는 배열 d
d = [10001] * 10001
d[0] = 0

# 최소한의 개수 세기
# 화폐마다 가치 m을 만들 수 있는 최소한의 개수를 세서 배열 d에 저장
for money in moneys:
    for i in range(m+1):
        # 기존값과 비교해서 더 작은 값을 d[i]에 저장
        d[i] = min(d[i], d[i-money] + 1)

if d[m] != 10001:
    print(d[m])
else:
    print(-1)

