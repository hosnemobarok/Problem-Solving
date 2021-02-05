# Sort the array using insertion sort
def insert(arr):
    # add code here

    size = len(arr)

    for i in range(size - 1):

        min_ind = i

        for j in range(i + 1, size):

            if arr[min_ind] > arr[j]:
                # swap arr[0] arr[1] number index value

                arr[j], arr[min_ind] = arr[min_ind], arr[j]


# {
#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        insert(arr)

        for i in range(n):
            print(arr[i], end=" ")

        print()
# } Driver Code Ends