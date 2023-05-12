n = int(input()) # 퇴사까지 남은 일수

# 일 테이블 만들기
work_table = [[0, 0]]
for i in range(n):
    tp = list(map(int, input().split()))
    work_table.append(tp)

dp = [0 for _ in range(n)]

def solve(i): # i일일 때, 벌 수 있는 돈의 최댓값
    if i > n: # 근무 일수를 넘어서면
        return 0
    else:
        if (i + work_table[i][0]) > n + 1:
            return solve(i+1)
        else:
            # 첫 번째 인자: i일에 근무하지 않는 경우
            # 두 번째 인자: i일에 근무하는 경우
            return max(solve(i+1), solve(i + work_table[i][0]) + work_table[i][1])

print(solve(1))
