output = []
for T in range(int(input())):
    string = input().split()    #string[0], position[1], number[2].

    if string[0] == "insert":   #string[0]
        output.insert(int(string[1]), int(string[2]))   #position[number]..insert hobe...

    elif string[0] == "remove":
        output.remove(int(string[1]))

    elif string[0] == "append":
        output.append(int(string[1]))

    elif string[0] == "sort":
        output.sort()

    elif string[0] == "pop":
        output.pop()

    elif string[0] == "reverse":
        output.reverse()

    elif string[0] == "print":
        print(output)
