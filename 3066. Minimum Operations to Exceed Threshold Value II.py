#https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        while nums[0] < k:
            count += 1
            x = nums.pop(0)
            y = nums.pop(0)
            t = x * 2 + y

            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < t:
                    left = mid + 1
                else:
                    right = mid
            nums.insert(left, t)

        return count
