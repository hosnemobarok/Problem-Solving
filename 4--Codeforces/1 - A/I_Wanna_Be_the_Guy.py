if __name__=="__main__":

	final_l = int(input())
	res = [x for x in range(1, final_l+1)]

	nums1 = list(map(int, input().split()))
	nums2 = list(map(int, input().split()))

	x = nums1[1:]
	y = nums2[1:]
	total_l = set(x + y)
	if sum(res) == sum(total_l):
		print("I become the guy.")
	else:
		print("Oh, my keyboard!")
