# problem link: https://www.codechef.com/YTPP001/problems/FDGHLM

def find_gcd(a,b):
    gcd = 1
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
           gcd = i
    return gcd

first, second = map(int, input().split())
lcm = first * second // find_gcd(first, second)
print(find_gcd(first, second), lcm)
