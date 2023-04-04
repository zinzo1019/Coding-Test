# 시험장 개수 입력받기
N = int(input())

# 시험 인원 입력받기
tester = list(map(int, input().split()))

# 감독 가능 인원수 입력받기
B, C = map(int, input().split())

#필요한 감독관 수
result = N # 시험장마다 총감독관은 무조건 존재해야 함

# 감독관 인원수 세기
for test in tester:
    test -= B # (시험 인원) - (총감독관의 감독 가능 인원수)
    if test > 0: # 총감독관만으로 감독이 불가능한 경우
        result += test // C
        if test % C: # 나머지가 존재한다면 감독관이 더 필요하다는 의미
            result += 1 # 감독관 한 명 더 추가

print(result)



