def Solution(nums):
	res = sorted(nums)
	print(*res)

if __name__=="__main__":
	size = int(input())
	nums = list(map(int, input().split()))
	Solution(nums)
