def Caps_Lock(string):

    # [1st formula] if blank string input
    if len(string) == 0: return string

    # [2nd formula] if single lowercase in input, convert to string upper
    if (len(string) == 1) and string[0].islower():
        return string.upper()

    # [3rd formula] complete string is uppercase, convert string lowers
    if string.isupper():
        return string.lower()

    # if first character is lowercase and mid char uppers and next char lowers
    # convert all char lower
    if (string[0].islower() and string[1:].isupper()):
        return string.capitalize()

    return string

if __name__ == '__main__':
    string = input()
    res = Caps_Lock(string)
    print(res)