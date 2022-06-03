# https://leetcode.com/submissions/detail/713503006/
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        Transpose = []
        for i in range(len(matrix[0])):
            sub_arr = []
            for j in range(len(matrix)):

                sub_arr += [matrix[j][i]]

            Transpose.append(sub_arr)

        return Transpose
