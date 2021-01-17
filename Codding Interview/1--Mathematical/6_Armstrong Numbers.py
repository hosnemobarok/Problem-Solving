def Armstrong_Numbers(number):
    temp = number
    arms_num = 0
    while number > 0:
        digit = number % 10
        arms_num += pow(digit, 3)
        number //= 10
    if temp == arms_num:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    number = int(input())
    res = Armstrong_Numbers(number)
    print(res)


'''
#User function Template for python3

#User function Template for python3
class Solution:
    def armstrongNumber (ob, n):
        # code here
        temp = n
        arms_num = 0
        while n > 0:
            digit = n % 10
            arms_num += pow(digit, 3)
            n //= 10

        if temp == arms_num:
            return 'Yes'
        else:
            return "No"


#{
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends
'''