#Dimikoj not accpet
T = int(input())
for i in range(T):
    S = input().split()
    for j in S:
        if j ==" ":
            continue
        print(j[::-1],end = ' ')
    print()



#2nd niom Dimikoj Accept
def reb(s):
	return s[::-1]
T = int(input())
for j in range(T):
	s=input()
	lis=s.split()
	string=' '
	for i in range(0,len(lis)):
		if i!=len(lis)-1:
			print(reb(str(lis[i])),end=' ')
		else:
			print(reb(str(lis[i])))