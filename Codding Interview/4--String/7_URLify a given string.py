def URLify_A_given_string(string):

    ref = string.lstrip().rstrip().replace(' ', '%20')
    return ref

# Drive Code
if __name__ == '__main__':
    for _ in range(int(input())):
        string = input()
        size = int(input())
        res = URLify_A_given_string(string)
        print(res)