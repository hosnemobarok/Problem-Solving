#Dimikoj Accept

def prime_number(a, b):
    li = [True] * 100002

    for x in range(0, 100002, 2):
        li[x] = False
    li[1], li[2] = False, True
    for xx in range(3, 320, 2):
        for xy in range(xx*xx, 100002, xx):
            li[xy] = False
    count = 0
    for itr in range(a, b+1):
        if li[itr]:
            count += 1
    print(count)

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    prime_number(a, b)




#2nd niom Hella vi Accept
def prime_numbers(a, b):
    li = [False if x % 2 == 0 else True for x in range(100002)]
    li[1], li[2] = False, True
    for i in range(3, int(100002**0.5), 2):
        for j in range(i*i, 100002, i): li[j] = False
    count = 0
    for i in range(a, b+1):
        if li[i]: count += 1
    print(count)

if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        a, b = map(int, input().split())
        prime_numbers(a, b)