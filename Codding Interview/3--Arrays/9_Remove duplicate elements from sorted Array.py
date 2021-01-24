# Sorted array remove duplicates
def remove_duplicates(arr):
    n = len(arr)

    # Best Case
    if n == 0 or n == 1:
        return n

    current_index = 1
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            arr[current_index] = arr[i]

            current_index += 1

    return current_index


if __name__ == '__main__':
    arr = [1, 1, 2, 2]
    l = remove_duplicates(arr)
    print(arr[:l])



'''
#User function template for Python

class Solution:	
	def remove_duplicate(self, A, N):
		# code here
		if N == 0 or N == 1:
		    return N
		    
		current_index = 1
		for i in range(1, N):
		    if A[i] != A[i-1]:
		        A[current_index] = A[i]
		        
		        current_index += 1
		        
		return current_index
        
#{ 
#  Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends
'''