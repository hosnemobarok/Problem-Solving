#Dimikoj Not Accept Runtime error
for T in range(int(input())):
    n1 = int(input())
    a = list(map(int, input().split()))
    n2 = int(input())
    b = list(map(int, input().split()))
    r = sorted(a+b)
    print(*r)


#2nd Rules
for T in range(int(input())):
	n1 = [int(i) for i in input().split()]
	del n1[0]
	n2 = [int(i) for i in input().split()]
	del n2[0]
	r = sorted(n1+n2)
	print(*r)


#3rd Rules
for T in range(int(input())):
    n1 = int(input())
    a = list(map(int, input().split()))
    n2 = int(input())
    b = list(map(int, input().split()))
    arr = sorted(a + b)
    for i in range(0, len(arr)):
        if (i < len(arr) - 1): # if(i != len(arr)-1:
            print(arr[i], end=' ')
        else:
            print(arr[i])

