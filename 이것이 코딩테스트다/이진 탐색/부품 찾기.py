"""
매장에는 n개의 부품이 있다.
어느 날 손님이 m개 종류의 부품을 구매하고자 한다.
이때 가게 안에 부품이 모두 있는지 확인하는 프로그램
순서대로, 있으면 yes, 없으면 no를 출력한다.
"""

# 매장
n = int(input())
store = list(map(int, input().split()))

# 손님
m = int(input())
customer = list(map(int, input().split()))

# 매장 부품 오름차순 정렬
store.sort()

# 이진 탐색 알고리즘
def search(array, target, start, end):
    # 시작과 끝이 역전되는 순간, 찾는 값이 없음을 의미
    if start > end:
        return False

    # mid는 시작과 끝의 중간 인덱스
    mid = (start + end) // 2

    # 중간값이 목표값과 같다면
    if array[mid] == target:
        return True

    # 중간값이 목표값보다 작다면
    elif target > array[mid]:
        # 중간 이후 값들을 재탐색
        return search(array, target, mid+1, end)

    else:
        # 중간 이전 값들을 재탐색
        return search(array, target, start, mid-1)

# 손님이 요구하는 부품을 하나씩 탐색
for target in customer:
    check = search(store, target, 0, n-1)
    if check:
        print("yes", end=' ')
    else:
        print("no", end=' ')