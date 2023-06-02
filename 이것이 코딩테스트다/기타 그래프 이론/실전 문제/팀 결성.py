"""
학교에서 학생들에게 0번부터 n번까지 번호 부여
이때 선생님은 '팀 합치기' 연산과 '같은 팀 여부 확인' 연산을 사용할 수 있다.
선생님이 m개의 연산을 수행할 수 있을 때, '같은 팀 여부 확인' 연산에 대한 연산 결과를 출력하는 프로그램을 작성하시오.
팀 합치기: 0
같은 팀 여부 확인: 1
"""

# 학생 수와 연산의 개수 입력받기
n, m = map(int, input().split())

# 부모 노드를 저장하는 배열
parent = []
# 자기 자신으로 부모노드 초기화
for i in range(n+1):
    parent.append(i)

# 최상위 부모 노드를 찾는 함수
def find_top(n):
    if parent[n] != n:
        parent[n] = find_top(parent[n])
    return parent[n]

# 팀 합치기 함수
def merge(n1, n2):
    n1_parent = find_top(n1)
    n2_parent = find_top(n2)
    if n1_parent > n2_parent:
        parent[n1_parent] = n2_parent
    else:
        parent[n2_parent] = n1_parent

# 결과를 저장할 배열
result = []

# 명령 입력받기
for _ in range(m):
    order, n1, n2 = map(int, input().split())
    # 같은 팀 여부 확인
    if order == 1:
        # 최상위 부모 노드 비교
        if find_top(n1) == find_top(n2):
            result.append("YES")
        else:
            result.append("NO")
    # 팀 합치기
    else:
        merge(n1, n2)

for i in result:
    print(i, end=' ')