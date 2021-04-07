def solve(string):
    res = ""
    for i in string:
        if i.isdigit():
            res += i
        else:
            res += " "

    li = list(map(int, res.split()))
    return sum(li)

if __name__ == '__main__':
    t = int(input())
    string = input()
    res = solve(string)
    print(res)