# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function
from itertools import *

for i,j in groupby(map(int,list(input()))):
    print(tuple([len(list(j)), i]) ,end = " ")
