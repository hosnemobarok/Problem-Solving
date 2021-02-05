'''
    Best Sorting algorithms is Merge sort.

    Time Complexity     : O(n log n)
    Space Complexity    : O(n)
'''


def Merge_Sort(li):
    # store li element size
    size = len(li)

    if size > 1:
        mid = size // 2

        left_arr = li[:mid]
        l_size = len(left_arr)

        right_arr = li[mid:]
        r_size = len(right_arr)

        # Sorting left_arr
        Merge_Sort(left_arr)

        # Sorting right_arr
        Merge_Sort(right_arr)

        i = j = k = 0

        while i < l_size and j < r_size:

            if left_arr[i] < right_arr[j]:

                li[k] = left_arr[i]
                i += 1
            else:
                li[k] = right_arr[j]
                j += 1

            k += 1

        while i < l_size:
            li[k] = left_arr[i]
            i += 1
            k += 1

        while j < r_size:
            li[k] = right_arr[j]
            j += 1
            k += 1

    return li


# {
#  Driver Code Starts
# Initial Template for Python 3

def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        mergeSort(arr, 0, n - 1)
        for i in range(n):
            print(arr[i], end=" ")
        print()
# } Driver Code Ends