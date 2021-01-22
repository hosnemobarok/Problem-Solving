# User function Template for python3

def sumElement(arr, n):
    # code here
    res = 0
    for i in range(n):
        res += arr[i]

    return res


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    testCase = int(input())

    for _ in range(testCase):
        n = int(input())
        arr = [int(x) for x in input().split()]

        print(sumElement(arr, n))
# } Driver Code Ends