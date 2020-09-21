#Dimikoj Accept

import math

T = int(input())
for i in range(T):
    N = int(input())
    s = int(math.sqrt(N))
    if (s * s) == N:
        print("YES")
    else:
        print("NO")






#2nd niom
t = int(input())

for _ in range(t):
	n = int(input())
	m = int(n ** 0.5)
	if m * m == n:
		print("YES")
	else:
		print("NO")