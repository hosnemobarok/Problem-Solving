# User function Template for python3

def saveIronman(s):
    # Complete the function
    res = s.replace(':', '', ).replace('?', '').replace('/', '').replace(',', '').replace(' ', '')

    return res.lower() == res.lower()[::-1]


# {
#  Driver Code Starts
# Initial Template for Python 3


for _ in range(0, int(input())):
    s = input()
    ans = saveIronman(s)
    if (ans == True):
        print("YES")
    else:
        print("NO")
# } Driver Code Ends



"""
# User function Template for python3

def saveIronman(s):
    # Complete the function

    res = ""
    for ch in s:
        if (ord(ch) >= 65 and ord(ch) <= 90) or (ord(ch) >= 97 and ord(ch) <= 122):
            res += ch

    return res.lower() == res.lower()[::-1]


# {
#  Driver Code Starts
# Initial Template for Python 3


for _ in range(0, int(input())):
    s = input()
    ans = saveIronman(s)
    if (ans == True):
        print("YES")
    else:
        print("NO")
"""