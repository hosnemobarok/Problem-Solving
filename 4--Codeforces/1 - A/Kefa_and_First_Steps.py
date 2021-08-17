
def Solution(nums):

    count = 0
    Max = 0
    for i in range(len(nums)-1):

        if nums[i] <= nums[i+1]:
            count += 1

            if count > Max:
                Max = count
        else:
            count = 0

    return Max + 1

if __name__=="__main__":
    size = int(input())
    nums = list(map(int, input().split()))

    res = Solution(nums)
    print(res)
