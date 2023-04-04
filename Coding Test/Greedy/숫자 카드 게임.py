n, m = map(int, input().split())

small_numbers = []

for i in range(n):
    number = list(map(int, input().split()))
    number.sort()
    small_numbers.append(number[0]) # 행 데이터 중 가장 작은 값들을 모음

small_numbers.sort()
print(small_numbers[n-1])