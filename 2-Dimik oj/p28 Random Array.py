# Dimikoj Accept

A = []
for _ in range(int(input())):
    A.append(int(input()))
B = sorted(A)
if A == B:
    print("YES")
else:
    print("NO")
