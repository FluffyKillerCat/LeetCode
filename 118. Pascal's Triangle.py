from typing import List

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        _ = [[1] * i for i in range(1, numRows + 1)]
        for i in range(len(_)):
            for j in range(len(_[i])):
                if i == 0 or j == 0 or (j == len(_[i]) - 1):
                    _[i][j] = 1
                else:

                    _[i][j] = _[i - 1][j - 1] + _[i - 1][j]
        return _
