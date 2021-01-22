def Second_Largest(arr, arr_size):
    if arr_size < 2:
        return

    first = second = -1

    for i in range(arr_size):

        if arr[i] > first:
            second = first
            first = arr[i]

        if arr[i] > second and arr[i] != first:
            second = arr[i]

    if second == -1:
        return 'all value same'
    else:
        return second


# Driver Code
if __name__ == '__main__':
    arr = [1, 10, 20, 1]
    # arr = [1, 1, -2, -2, 2, 4]
    arr_size = len(arr)

    res = Second_Largest(arr, arr_size)
    print(res)

'''
#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
		# code here

        first = second = -1
        for i in range(n):

            if arr[i] > first:
                second = first
                first = arr[i]

            if arr[i] > second and arr[i] != first:
                second = arr[i]

        if second == -1:
            return -1

        else:
            return second


#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
'''