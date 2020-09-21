#Dimikoj Accpet:- problem NO:-29

T = int(input())
for i in range(T):
    ch = input()
    r = ord(ch)
    if r >= 65 and r <= 90:
        print('Uppercase Character')
    elif r >= 97 and r <= 122:
        print('Lowercase Character')
    elif r >= 48 and r <= 57:
        print('Numerical Digit')
    else:
        print('Special Character')



#2nd Rules
for i in range(int(input())):
	S=input()
	if S.islower():print("Lowercase Character")
	elif S.isupper():print("Uppercase Character")
	elif S.isdigit():print("Numerical Digit")
	else:print("Special Character")