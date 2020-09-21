#Dimikoj Accept
N = int(input())
a,b,c = 1, 1, 2
for c in range(N-2):
    a,b = b, a+b
print(b)





#2nd Rules
t = int(input())
n1 = 0
n2 = 1
c = 0
while c < t:
    print(n1,end=',')
    nth = n1+n2
    n1 = n2
    n2 = nth
    c += 1



#3rd Rules
fib_x = 1
fib_next = 1
N = int(input())
if N <= 2:
    fib_n = 1
else:
    i = 3
    while i<= N:
        i += 1
        fib_temp = fib_x + fib_next
        fib_x = fib_next
        fib_next = fib_temp
    fib_n = fib_next
print(fib_n)