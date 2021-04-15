# Accept
def A_Solve():
    s = input()
    count = 0
    for i in s.lower():
        if i == 'a' or i == 'e' or i== 'i' or i == 'o' or i == 'u':
            count += 1
    print(count)

def B_Solve():
  pass

# Accept
def C_Solve():
    for index in range(int(input())):
        N, H, K, X = map(int, input().split())

        mid_h = K // N

        if mid_h / H > X:
            print(f"{mid_h} YES")
        else:
            print(f"{mid_h} NO")

def D_Solve():
    pass

def E_Solve():
    pass

# Accept
def F_Solve():
    for index in range(int(input())):

        num = int(input())
        num_mid = num // 2

        sum_arr = []
        for el in range(num_mid + 1):
            if el == 0 or el == num_mid:
                print("*" * num)

            elif el < num_mid:
                out = "*" + (' ' * (el - 1)) + '*' + ' ' * (num_mid - el - 1) + '*' + ' ' * (num_mid - el - 1) + "*" + (' ' * (el - 1)) + "*"
                sum_arr.append(out)
                print(out)

        for el in range(num_mid - 2, -1, -1):
            string = ''
            for j in sum_arr[el]:
                string += j
            print(string)
        print("*" * num)
        print()


#A_Solve()
#B_Solve()
#C_Solve()
#D_Solve()
#E_Solve()
#F_Solve()

