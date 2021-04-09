# Enter your code here. Read input from STDIN. Print output to STDOUT
n_size = int(input())
a = set(map(int, input().split()))

s_size = int(input())
b = set(map(int, input().split()))
res = a.intersection(b) or a & b
print(len(res))
