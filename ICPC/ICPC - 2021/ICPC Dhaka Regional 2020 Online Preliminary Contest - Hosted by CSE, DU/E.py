def maxSubArray(nums):
    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
    # print(dp)
    return max(dp)


def selectionSort2(nums):
    ans = 0
    tracker = 0

    maxNum = maxSubArray(nums)
    if maxNum > ans:
        ans = maxNum
        tracker = 0

    for i in range(len(nums)):

        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
        print(nums)
        maxNum = maxSubArray(nums)
        if maxNum > ans:
            ans = maxNum
            tracker = i

    return (ans, tracker)


def solution():
    t = int(input())
    for index in range(1, t + 1):
        n = int(input())
        nums = list(map(int, input().split()))
        ans, tracker = selectionSort2(nums)
        print("Case {}: {} {}".format(index, ans, tracker))


solution()