# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())

# 부모 테이블을 자기 자신 노드로 초기화
table = []
for i in range(v+1):
    table.append(i)

# 최상위 부모 노드를 찾아서 반환
def get_top_node(node):
    # 특정 노드의 부모 노드를 가져옴
    parent = table[node]
    # 만약 최상위 노드가 아니라면
    if parent != table[parent]:
        parent = get_top_node(parent)
    return parent

# 합치기 함수
def union(n1, n2):
    # 각 노드의 부모 노드를 찾기
    parent1 = get_top_node(n1)
    parent2 = get_top_node(n2)

    # 각 노드의 부모 노드 중 더 작은 값을 최상위 부모 노드로 설정
    if parent1 < parent2:
        # 부모 노드 테이블 업데이트
        table[n2] = parent1
    else:
        table[n1] = parent2

# 간선 정보 입력받기
for i in range(e):
    n1, n2 = map(int, input().split())
    union(n1, n2)

# 출력하기
print("각 원소가 속한 집합:", end=' ')
for i in range(1, v+1):
    # 최상위 부모 노드만 출력
    print(get_top_node(i), end=' ')


