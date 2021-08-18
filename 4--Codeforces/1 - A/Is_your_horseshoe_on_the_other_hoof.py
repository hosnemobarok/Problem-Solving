def solution(s1, s2, s3, s4):

	li = [s1, s2, s3, s4]
	conv = set(li)
	n = len(li)
	s = len(conv)
	if n == s:
		return 0
	else:
		return n - s


if __name__=="__main__":
	s1, s2, s3, s4 = map(int, input().split())
	res = solution(s1, s2, s3, s4)
	print(res)
