def solution(nums):
    return min(len(nums) / 2, len(set(nums)))

nums = [3, 1, 2, 3]
print(int(solution(nums)))