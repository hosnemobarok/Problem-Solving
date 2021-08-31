def A1():
    with open('A1.txt', 'w') as output:
        test = int(input())
        for case in range(1, test+1):
            string = input().upper()

            all_Ltters = [0] * 26
            high_Vowel = 0
            high_Consonant = 0

            all_Vowel = ["A", "E", "I", "O", "U"]

            hight_VowelChr = 0
            high_ConsonantChr = 0


            for ch in string:
                all_Ltters[ord(ch) - 65] += 1

                if ch in all_Vowel:
                    if all_Ltters[ord(ch) - 65] > high_Vowel:
                        high_Vowel = all_Ltters[ord(ch) - 65]
                        hight_VowelChr = ord(ch) - 65

                else:
                    if all_Ltters[ord(ch) - 65] > high_Consonant:
                        high_Consonant = all_Ltters[ord(ch) - 65]
                        high_ConsonantChr = ord(ch) - 65

            consonantC = 0
            vowelC = 0

            for c in string:
                if c in all_Vowel:

                    if c != chr(hight_VowelChr + 65):
                        vowelC += 2
                    consonantC += 1

                else:
                    if c != chr(high_ConsonantChr + 65):
                        consonantC += 2
                    vowelC += 1

            result = min(consonantC, vowelC)
            output.write("Case #%d: %d\n"%(case, result))

A1()