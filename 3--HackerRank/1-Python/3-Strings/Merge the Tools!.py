def merge_the_tools(string, k):
    string_lenth = len(string)
    for i in range(0, string_lenth, k):
        s = string[i: i + k]

        u = []
        for j in s:
            if j not in u:
                u.append(j)
        print(''.join(u))

