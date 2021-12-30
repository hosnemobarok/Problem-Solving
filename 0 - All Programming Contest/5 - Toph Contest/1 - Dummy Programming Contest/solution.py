"""
	case 1: n % 2 == 0 -> fizz
	case 2: n % 5 == 0 -> buzz
	case 3: (n % 2) == 0 and (n % 5) == 0 -> fizzbuzz
	case 4: (n % 2) != 0 or (n% 5) != 0 -> sad
	
	Input	|	Output
	------------------
	14		|	fizz
	25		|	buzz
	10		| 	fizzbuzz
	33		|	sad
	
"""

# Problem link: https://toph.co/arena?practice=61cdf857969d3c6a532b4135#!/p/61728cf2632c5d4aa196fa43
# Accept
def solution():
	n = int(input())
	if (n % 2) == 0 and (n % 5) == 0:
		print("fizzbuzz")
	
	elif (n % 2) == 0:
		print("fizz")
	
	elif (n % 5) == 0:
		print("buzz")
		
	elif (n % 2) != 0 or (n % 5) != 0:
		print("sad")
		
			
solution()
	
	