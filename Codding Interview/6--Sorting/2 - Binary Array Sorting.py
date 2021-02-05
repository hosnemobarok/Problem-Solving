# User function Template for python3


##Complete this function
def binSort(arr, n):
    # Your code here
    return arr.sort()


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        N = int(input())
        A = list(map(int, input().split()))

        binSort(A, N)

        for i in A:
            print(i, end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends