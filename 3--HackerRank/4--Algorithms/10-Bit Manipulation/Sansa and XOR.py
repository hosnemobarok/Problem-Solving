class Solution(object):
    def S_Xor(arr, n):
        res = 0
        if n % 2 == 1:
            for i in range(0, n, 2):
                res ^= arr[i]
            return res
        return 0


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        res = Solution.S_Xor(arr, n)
        print(res)
