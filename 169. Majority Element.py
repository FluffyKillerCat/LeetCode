from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        t = 0
        ans = 0
        a = set(nums)
        for num in a:
            if nums.count(num) > len(nums) / 2:
                return num



if __name__ == '__main__':
    s = Solution()
    ans = s.majorityElement([1,1,1,2])
    print(ans)