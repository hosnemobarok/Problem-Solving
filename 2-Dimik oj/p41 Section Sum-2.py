#dimik oj Accept

for T in range(int(input())):
    n = int(input())
    res = 0
    fact = 1
    for i in range(1, n+1):
        fact *= i
        res += i/ fact
    print('%.4f'%res)



#2nd Rules

#function use code
    '''
        1/1!+ 2/2!+ 3/3! +....n/n! = sum
    '''
def sumOfSeries(num):
    # Computing MAX
    res = 0
    fact = 1

    for i in range(1, num + 1):
        fact *= i
        res += (i / fact)

    return res

n = int(input())
print("Sum: ", sumOfSeries(n))
