'''
    Time Complexity     : O(n)
    Space Complexity    : O(1)
'''


def Linear_Search(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i + 1

    return 'sorry target is not found!'


if __name__ == '__main__':
    for _ in range(int(input())):
        arr = list(map(int, input().split()))
        target = int(input())
        res = Linear_Search(arr, target)
        print(res)

'''
#User function Template for python3
class Solution:


	def search(self,arr, n, k): 
    	# code here
    	for i in range(n):
    	    if arr[i] == k:
    	        return i+1
    	return -1


#{ 
#  Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n, k=map(int, input().strip().split())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.search(arr, n, k)
        print(ans)
        tc=tc-1
# } Driver Code Ends
'''