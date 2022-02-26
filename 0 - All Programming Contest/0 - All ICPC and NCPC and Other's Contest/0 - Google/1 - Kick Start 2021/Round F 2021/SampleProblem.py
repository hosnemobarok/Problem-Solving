 # Problem link: --> https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000942404#problem
 
def SampleProblem():
	test  = int(input())
	for case in range(1, test+1):
		b, k = map(int, input().split())
		m = list(map(int, input().split()))
		
		total_candy = sum(m)
		
		res = total_candy % k
		print("Case #%d: %d"%(case, res))
			
			
SampleProblem()		