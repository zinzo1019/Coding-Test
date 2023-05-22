# 학생의 수
n = int(input())

# 성적 입력받기
array = []
for i in range(n):
    array.append(input().split())

# 성적을 기준으로 하는 함수
def setting(data):
    return data[1]

# 성적이 낮은 순으로 정렬하기
array = sorted(array, key=setting)

# 이름만 출력하기
for i in range(n):
    print(array[i][0], end=' ')