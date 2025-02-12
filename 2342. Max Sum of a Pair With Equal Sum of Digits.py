from collections import defaultdict
from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        max_total = -1
        digit_sum_groups = defaultdict(list)
        print(digit_sum_groups)
        for num in nums:
            digit_sum = sum(int(digit) for digit in str(num))
            digit_sum_groups[digit_sum].append(num)
        sorted_groups = sorted(digit_sum_groups, reverse = True)
        for digit_sum in digit_sum_groups.values():
            if len(digit_sum) >=2:
                sorted_vals = sorted(digit_sum, reverse = True)
                total = sum(sorted_vals[:2])
                max_total = max(max_total, total)
        return max_total


print(Solution().maximumSum([18,43,36,13,7]))