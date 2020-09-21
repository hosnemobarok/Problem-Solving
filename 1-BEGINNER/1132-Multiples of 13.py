#not Accept
X = int(input())
Y =  int(input())
sum = 0
for i in range(X, Y+1):
    if i % 13 != 0:
        sum += i
print(sum)