# https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        answer = []

        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                answer.insert(i-1, "FizzBuzz")
            elif i % 5 == 0:
                answer.insert(i, "Buzz")
            elif i % 3 == 0:
                answer.insert(i-1, "Fizz")
            else:
                answer.insert(i-1, str(i))

        return answer
