def string_sort(string):
    res = sorted(string)
    print(*res[::-1], sep='')


if __name__ == '__main__':
    for _ in range(int(input())):
        string = input()
        string_sort(string)