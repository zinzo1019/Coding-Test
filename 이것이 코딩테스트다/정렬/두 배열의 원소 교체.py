"""
배열 A와 배열 B의 원소를 골라 교체
배열 A의 모든 원소의 합이 최대가 되도록
n: 원소의 개수
k: 교체 쵯수
"""

n, k = map(int, input().split())

# 배열 입력받기
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

# 배열 A 오름차순 정렬
array_a = sorted(array_a)
# 배열 B 내림차순 정렬
array_b = sorted(array_b, reverse=True)

# 최대 k번 교체
for i in range(k):
    # 만약 배열 A의 원소가 배열 B의 원소보다 작다면 교체하지 않음
    if array_a[i] < array_b[i]:
        array_a[i], array_b[i] = array_b[i], array_a[i]

# 배열 A의 원소의 합
print(sum(array_a))




