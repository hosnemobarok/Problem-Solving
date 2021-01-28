'''
Input:
S = i.like.this.program.very.much

Output: much.very.program.this.like.i

Input:
S = pqr.mno

Output: mno.pqr
'''

def Reverse_word(string):
    res = string.replace('.',' ').split()[::-1]
    ress = ""
    for i in res:
        ress += i.__add__('.')
    return ress[:-1]

# Driver Code
if __name__ == '__main__':
    string = input()
    res = Reverse_word(string)
    print(res)


'''
# User function Template for python3

def reverseWords(S):
    # code here 
    res = S.replace('.',' ').split()[::-1]
    ress = ""
    for i in res:
        ress += i.__add__('.')
    return ress[:-1]


#{ 
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        print(reverseWords(s))

# } Driver Code Ends
'''