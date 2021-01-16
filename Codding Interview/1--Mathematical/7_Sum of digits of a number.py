# Iterative Solution
# Function to get sum of digits
def SumOfdigit(num):

    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num //= 10

    print(sum)

# Driver code
if __name__ == '__main__':
    num = int(input())
    SumOfdigit(num)




# Recursive Solution
def SumOfdigit(num):

    if num == 0:
        return 0
    else:
        return (num % 10) + SumOfdigit(num // 10)

# Driver Code
if __name__ == '__main__':
    num = int(input())
    print(SumOfdigit(num))



'''

# User function Template for python3

class Solution:
    def isDigitSumPalindrome(self, N):
        sum = 0

        while N > 0:
            digit = N % 10
            sum += digit
            N //= 10

        str_sum = str(sum)
        if str_sum[::-1] == str(sum):
            return 1
        else:
            return 0


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isDigitSumPalindrome(N))
# } Driver Code Ends

'''
