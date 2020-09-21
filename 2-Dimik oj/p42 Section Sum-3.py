#Dimikoj Accept

T = int(input())
for f in range(T):
	n = int(input())
	s = ""
	for i in range(n, -1, -1):
		if i ==1:
			s = s+"2 + "
			continue
		if i==0:
				s = s+"1"
				break
		s = s+("2^%d + ")%(i)
	print(s)