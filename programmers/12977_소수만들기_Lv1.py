from itertools import combinations
import math
# nums = [1, 2, 3, 4]
nums = [1, 2, 7, 6, 4]

def sosu(a):
	if a == 1:
		return False
	else:
		for i in range(2, int(math.sqrt(a))+1):
			if a % i == 0:
				return False
	return True

def solution(nums):
	answer = 0
	for num in combinations(nums, 3):
		if sosu(sum(num)):
			answer += 1
	return answer

print(solution(nums))