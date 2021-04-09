marklist = []
scorelist = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())

        marklist += [[name, score]]
        scorelist +=[score]
    s = sorted(list(set(scorelist)))[1]

    for a,c in sorted(marklist):
        if c == s:
            print(a)
