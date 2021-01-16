# Reverse digit
def reverse_digit(number):

    rev_num = 0
    while number > 0:

        lastDigit = number % 10
        rev_num = (rev_num * 10) + lastDigit
        number //= 10

    print(rev_num)


# Driver Code
if __name__ == '__main__':

    number = int(input())
    reverse_digit(number)



'''
#User function Template for python3

class Solution:
	def reverse_digit(self, n):
	    
	    reverse = 0
	    
	    while n > 0:
	        lastDigit = n % 10
	        reverse = (reverse * 10) + lastDigit
	        
	        n //= 10
	        
	    return reverse



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.reverse_digit(n)
		print(ans)
# } Driver Code Ends
'''