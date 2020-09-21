#Dimikoj Accept

import  math
for T in range(int(input())):

	x1,y1 = map(float, input().split())
	r = float(input())
	x2,y2 = map(int, input().split())

	s = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
	if r > s:
		print("The point is inside the circle")
	else:
		print('The point is not inside the circle')