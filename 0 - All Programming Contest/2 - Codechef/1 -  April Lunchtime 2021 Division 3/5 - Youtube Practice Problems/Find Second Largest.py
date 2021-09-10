# problem link: https://www.codechef.com/YTPP001/problems/SECLAR
a = int(input())
b = int(input())
c = int(input())

li = [a, b, c]
li.remove(max((li)))
print(max(li))