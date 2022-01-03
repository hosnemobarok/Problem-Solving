# Problem link:-> https://leetcode.com/problems/number-of-different-integers-in-a-string/
# not accept

def solution():
	
	word = input()
	just_digit = ""
	
	for i in word:
		if i.isdigit():
			just_digit += i
		else:
			just_digit += " "
			
	digit_list = just_digit.split()	
	
	result = ""
	for wd in digit_list:
		
		single_word = wd		
		if single_word[0]:
			
			last_zero_index = 0
			one_index = 0
			
			for ch in single_word:
				if ch == "0":
					last_zero_index += 1
				
				else:
					# one zero index
					one_index = last_zero_index
					break
			
			result += single_word[one_index:] + " "
					
		
		else:
			result += single_word + " "
		
	
	solve = set(result.split())
	print(len(solve))
		
	
solution()