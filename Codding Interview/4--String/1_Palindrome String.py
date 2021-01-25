'''
    Time Complexity     : O(n)
    Space Complexity    : O(1)
'''
def Palindrome_String(string):

    for i in range(0, len(string)//2):
        print(string[i], '=', string[len(string) - i - 1])
        if string[i] != string[len(string)-i-1]:


            return 'No'

    return 'Yes'


if __name__ == '__main__':
    string = input()
    res = Palindrome_String(string)
    print(res)


'''
#User function Template for python3
class Solution:
	def isPlaindrome(self, S):
		# code here
		if S == S[::-1]:
		    return 1
		else:
		    return 0



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPlaindrome(S)
		print(answer)

# } Driver Code Ends
'''