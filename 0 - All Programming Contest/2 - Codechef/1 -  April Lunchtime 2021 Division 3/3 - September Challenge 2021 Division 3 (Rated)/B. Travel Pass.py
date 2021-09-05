# link: https://www.codechef.com/SEPT21C/problems/TRAVELPS
# Accept
def B_solve():
    for case in range(int(input())):
        n, a, b = map(int, input().split())
        binary_string = input()

        total_one = binary_string.count("1") * b
        total_zero = binary_string.count("0") * a

        res = total_one + total_zero
        print(res)

B_solve()