#B solve
li = ["ABC","ARC", "AGC", "AHC"]
s1 = input()
s2 = input()
s3 = input()

inp = [s1, s2, s3]
res = list(set(li) ^ set(inp))
print(*res)