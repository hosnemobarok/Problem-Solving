def Find_First_Repeated_Character(string):
    if len(string) < 1:
         return -1

    first_repeated_chr = ''
    rep = ''
    for i in range(len(string)):
         if string[i] not in first_repeated_chr:
              first_repeated_chr += string[i]

         else:
              rep += string[i]

    if len(rep) >= 1:
         return rep[0]
    else:
         return -1



if __name__=="__main__":
    for _ in range(int(input())):
        string = input()
        res = Find_First_Repeated_Character(string)
        print(res)