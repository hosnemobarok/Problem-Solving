from itertools import combinations
S,k = input().split()
for j in range(1,int(k)+1):
    for i in combinations(sorted(S),j):
        print("".join(i))
