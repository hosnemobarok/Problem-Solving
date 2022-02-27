# problem link: - https://cses.fi/problemset/task/1069/
 
def repetitionsSolution():
    string = input()

    count = 0
    max = 0

    for i in range(len(string) - 1):

        if string[i] == string[i + 1]:
            count += 1

            if max <= count:
                max = count
        else:
            count = 0

    print(max+1)


repetitionsSolution()
