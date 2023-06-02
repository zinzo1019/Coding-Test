"""
동빈이는 총 n개의 강의를 듣고자 한다.
모든 강의는 1번부터 n번까지의 번호를 가진다.
또한 동시에 여러 개의 강의를 들을 수 있다고 가정한다.
n개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 각각 출력하시오.
"""

# 강의 n개 입력받기
import copy

n = int(input())

# 진입차수를 저장하는 배열
indegree = [0] * (n+1)

#  수강 시간을 저장하는 배열
time = [0] * (n+1)

# 커리큘럼의 관계를 그래프 형태로 저장
graph = [[] for _ in range(n+1)]

# 과목 시간과 선수 과목 입력받기
for subject in range(1, n+1):
    data = list(map(int, input().split()))
    # 수강 시간 저장
    time[subject] = data[0]
    for i in data[1:-1]:
        # 진입 차수 저장
        indegree[subject] += 1
        # 선수 과목 저장
        graph[i].append(subject)

# 위상 정렬
def topological():

    # 결과
    result = copy.deepcopy(time)

    queue = []
    # 진입차수가 0이면 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)

    # 큐가 빌 때까지 반복
    while queue:
        now = queue.pop()
        for node in graph[now]:
            # 더 큰 값을 선택해야 모든 선수과목을 수강하고 다음 과목 수강 가능
            result[node] = max(result[node], result[now] + time[node])
            # 진입차수 1 줄이기
            indegree[node] -= 1
            # 만약 진입차수가 0이면 큐에 삽입
            if indegree[node] == 0:
                queue.append(node)
    print(result)

topological()