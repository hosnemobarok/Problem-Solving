def Reverse_Bits(num):

	conv_b = bin(num)[2:][::-1]
	return int(conv_b, 2)


if __name__=="__main__":
	while True:
		num = int(input())
		res = Reverse_Bits(num)
		print(res)
