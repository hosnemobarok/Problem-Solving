def Non_Repeating_Character(string):
    single_lettler = ''
    repeating_lettler = ''

    non_repeating_lettler = ''

    for i in string:
        if i not in single_lettler:

            single_lettler += i

        else:
            repeating_lettler += i


    for i in single_lettler:
        if i not in repeating_lettler:
            non_repeating_lettler += i


    if len(single_lettler) == len(repeating_lettler):
        return '$'
    else:
        return non_repeating_lettler[0]


if __name__ == '__main__':
    #for _ in range(int(input())):
        string = input()
        res = Non_Repeating_Character(string)
        print(res)












"""
# User function Template for python3

'''
	Your task is to return the index of lefmost non-repeating
	character or return
	-1 if all characters occur more than once.

	Function Arguments: s (given string)
	Return Type: integer
'''


def nonrepeatingCharacter(s):
    single_lettler = ''
    repeating_lettler = ''

    non_repeating_lettler = ''

    for i in s:
        if i not in single_lettler:

            single_lettler += i

        else:
            repeating_lettler += i

    for i in single_lettler:
        if i not in repeating_lettler:
            non_repeating_lettler += i



    if len(single_lettler) == len(repeating_lettler):
        return '$'

    else:
        return non_repeating_lettler[0]


# {
#  Driver Code Starts
# Initial Template for Python


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        ans = nonrepeatingCharacter(s)
        if (ans != '$'):
            print(ans)
        else:
            print(-1)

# } Driver Code Ends
"""