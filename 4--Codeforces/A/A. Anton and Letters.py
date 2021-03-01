def Anton_Letters(s):
    for i in ', {}':
        s.discard(i)

    return len(s)

if __name__ == '__main__':
    s = set(input())
    print(Anton_Letters(s))