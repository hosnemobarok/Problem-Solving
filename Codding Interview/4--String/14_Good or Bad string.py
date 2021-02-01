def Good_or_Bad_string(string):

    count_con = 0
    count_vowel = 0

    vowel = 'aeiou'

    for i in string:
        if i in vowel:
            count_con = 0
            count_vowel += 1

        if i == "?":
            count_con += 1
            count_vowel += 1

        else:
            count_vowel = 0
            count_con += 1

        if count_vowel > 5 or count_con > 3:
            return 0

    else:
        return 1


if __name__ == '__main__':
    for _ in range(int(input())):
        string = input()
        res = Good_or_Bad_string(string)
        print(res)


