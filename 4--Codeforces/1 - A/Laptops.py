res = "Poor Alex"
for i in range(int(input())):
	a, b = map(int, input().split())
	
	if a < b:
		res = "Happy Alex"

print(res)