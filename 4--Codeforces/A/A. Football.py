def Football(string):

    substr_1 = '1'*7
    substr_0 = '0'*7

    if substr_1 in string or substr_0 in string:
        return "YES"

    return "NO"


if __name__ == '__main__':
    string = input()
    res = Football(string)
    print(res)

"""
def Football(string):

    x, y, z = 0, 0, 0
    for i in range(len(string)):
        if string[i] == '1':
            x += 1
        
        else:
            y += 1
            
        if x == 7 or y == 7:
            z = 1
    if z == 1:
        return "YES"
    return "NO"


if __name__ == '__main__':
    string = input()
    res = Football(string)
    print(res)
"""