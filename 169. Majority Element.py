from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        t = 0

        a = set(nums)
        for num in a:
            if nums.count(num) > len(nums) / 2:
                return num



if __name__ == '__main__':
    s = Solution()
    ans = s.majorityElement([1,1,1,2])
    print(ans)


nums = [1,1,1,2,3,4,5,6,7,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
res = -1
count = 0
for num in nums:
    if num == res:
        count += 1
    else:
        if count == 0:
            res = num
            count += 1
        else:
            count -= 1
print(res, count)