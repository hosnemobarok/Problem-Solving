# contest link: https://www.codechef.com/SNCKQL21?order=desc&sortBy=successful_submissions
def Lucky_Number():
    for _ in range(int(input())):
        a, b, c =  map(int, input().split())

        if 7 in [a, b, c]:
            print("YES")
        else:
            print("NO")


#Lucky_Number()


def Test_Match_Series():
    for _ in range(int(input())):
        a, b, c, d, e = map(int, input().split())
        li = [a, b, c, d, e]
        INDIA = li.count(1)
        ENGLAND = li.count(2)

        if INDIA == ENGLAND:
            print("DRAW")
        elif INDIA > ENGLAND:
            print("INDIA")
        else:
            print("ENGLAND")

#Test_Match_Series()



