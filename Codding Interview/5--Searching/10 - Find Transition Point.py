def transitionPoint(arr, n):
    # Code here
    if 1 not in arr:
        return -1

    return arr.count(0)


# {
#  Driver Code Starts
# driver code
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))

# } Driver Code Ends