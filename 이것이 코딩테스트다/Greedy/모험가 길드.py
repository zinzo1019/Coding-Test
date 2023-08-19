"""
모험가 n명의 공포도 측정
공포도가 x인 모험가는 반드시 x명 이상으로 구성된 모험가 그룹에 참여해야 여행을 떠날 수 있다.
일부 모험가는 마을에 그대로 남아 있어도 될 때, 여행을 떠날 수 있는 그룹의 최댓값을 구하시오.
"""

# 모험가 수 n 입력받기
n = int(input())

# 모험가의 공포도 입력받기
people = list(map(int, input().split()))
# 공포도 오름차순 정렬
people.sort()

# 결과
result = 0
# 팀원수
member = 0

# 사람수만큼 반복
for fear in people:
    member += 1
    if member == fear:
        result += 1
        member = 0

print(result)