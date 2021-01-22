
# Minimum Function
def getMin(arr, n):
	res = arr[0]
	for i in range(1,n):
		res = min(res, arr[i])
	return res

# Maximum Function
def getMax(arr, n):
	res = arr[0]
	for i in range(1,n):
		res = max(res, arr[i])
	return res

# Driver Program
arr = [12, 1234, 45, 67, 1]
n = len(arr)
print ("Minimum element of array:", getMin(arr, n))
print ("Maximum element of array:", getMax(arr, n))

# This code is contributed
# by Shreyanshi Arun.










'''# User function Template for python3

def getMinMax(a, n):
    return min(a), max(a)


# {
#  Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]

        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends'''