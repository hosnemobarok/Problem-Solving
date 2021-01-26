"""
Example:
    |Input:   |    Output: |
    |---------|------      |
    |2        |            |
    |----------------------|
    |Hello Bye|-- HBeylelo |
    |         |            |
    |abc def  |-- adbecf   |

"""
def Merge_two_strings(s1, s2):

    size = [len(s1), len(s2)]
    s1_l, s2_l = size[0], size[1]


    if s1_l > s2_l:
        res = s1[s2_l:]
    else:
        res = s2[s1_l:]

    merge = ""
    for i in range(min(size)):
        merge += s1[i]
        merge += s2[i]

    return merge+res


# Driver Code
if __name__ == "__main__":
    for _ in range(int(input())):
        s1, s2 = input().split()
        res = Merge_two_strings(s1, s2)
        print(res)
