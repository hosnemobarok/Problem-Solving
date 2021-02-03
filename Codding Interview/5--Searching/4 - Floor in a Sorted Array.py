# User function Template for python3

# Complete this function
def findFloor(A, N, X):
    # Your code here

    count = 0
    for i in range(N - 1):
        if A[i] < X:
            count += 1

    if count > 0:
        return count
    else:
        return -1


# {
#  Driver Code Starts
# Initial Template for Python 3


import math


def main():
    T = int(input())
    while (T > 0):
        NX = [int(x) for x in input().strip().split()]
        N = NX[0]
        X = NX[1]

        A = [int(x) for x in input().strip().split()]

        print(findFloor(A, N, X))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends