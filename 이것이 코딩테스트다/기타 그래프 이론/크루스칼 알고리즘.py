# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())

# 부모 테이블을 자기 자신 노드로 초기화
table = []
for i in range(v+1):
    table.append(i)

# 최상위 부모 노드를 찾아서 반환
def get_top_node(node):
    # 만약 최상위 노드가 아니라면
    if table[node] != node:
        node = get_top_node(table[node])
    return node

# 합치기 함수
def union(n1, n2):
    # 각 노드의 부모 노드 중 더 작은 값을 최상위 부모 노드로 설정
    parent1 = get_top_node(n1)
    parent2 = get_top_node(n2)
    if parent1 < parent2:
        # 부모 노드 테이블 업데이트
        table[parent2] = parent1
    else:
        table[parent1] = parent2

# 간선 정보를 저장하는 배열
edges = []

# 간선 정보 입력받기
for _ in range(e):
    node1, node2, cost = map(int, input().split())
    edges.append((cost, node1, node2))

# 오름차순 정렬
edges.sort()

# 최소 비용을 저장할 변수
result = 0

for edge in edges:
    cost, n1, n2 = edge
    # 사이클이 생성되지 않는다면
    if get_top_node(n1) != get_top_node(n2):
        union(n1, n2)
        result += cost

print(result)