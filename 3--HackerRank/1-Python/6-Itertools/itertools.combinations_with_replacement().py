# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *
S, k = input().split()
for i in combinations_with_replacement(sorted(S),int(k)):
    print("".join(i))
