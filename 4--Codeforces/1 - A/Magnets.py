def Solution(arr):

	count = 1
	for i in range(len(arr)-1):
		if arr[i] != arr[i+1]:
			count += 1

	return count

if __name__=="__main__":
	arr = []
	for _ in range(int(input())):
		num = int(input())
		arr.append(num)
	
	print(Solution(arr))
