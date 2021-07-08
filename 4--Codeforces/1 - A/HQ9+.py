def solution(string):
	
	for ch in string:

		if ch == "H" or ch == "Q" or ch == "9":
			return "YES"
		
	else:
		return "NO"
		
			
if __name__=="__main__":
	string = input()
	res = solution(string)
	print(res)
