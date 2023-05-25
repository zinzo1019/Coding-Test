"""
절단기 길이 h
길이가 h보다 긴 떡은 잘리고, 길지 않은 떡은 잘리지 않는다.
잘린 떡의 길이만큼 손님이 가져가며,
손님이 요청한 총 길이가 m일 때, m만큼의 떡을 얻기 위해 설정할 수 있는 길이의 최댓값을 구하라.
"""

# 떡의 개수 n과 손님 요청 길이 m
n, m = map(int, input().split())

# 떡의 길이
rice_cake = list(map(int, input().split()))

# 떡 자르기 
# 잘린 떡의 길이 리턴
def cut(height):
    # 손님이 가져가는 떡의 길이
    total = 0
    # 떡 자르기 시작
    for rice in rice_cake:
        # 만약 떡의 길이가 절단기보다 작거나 같다면 넘어간다.
        if rice <= height:
            continue
        # 아니라면 자르고 손님이 가져간다.
        else:
            rice -= height
            total += rice
    return total

# 떡의 길이 오름차순 정렬
rice_cake.sort()

# 절단기의 길이마다 잘린 떡의 길이의 합을 저장
height_array = []
for h in range(rice_cake[0], rice_cake[n-1], 1):
    height_array.append((h, cut(h)))

# 잘린 떡의 길이의 합을 기준으로 오름차순
def setting(data):
    return data[1]
height_array.sort(key=setting)

# 최댓값 구하기
def insert_sort(target):
    index = 0
    for i in height_array:
        if i[1] < target:
            index += 1
        else:
            return index

print(height_array[insert_sort(m)][0])