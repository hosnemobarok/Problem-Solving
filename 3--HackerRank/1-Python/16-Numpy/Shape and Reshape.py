import numpy
arr = list(map(int,  input().split()))
res = numpy.array(arr).reshape(3, 3)
print(res)
