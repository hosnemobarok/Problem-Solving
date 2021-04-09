# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())
res = divmod(a, b)
for i in res:
    print(i)
print(res)
