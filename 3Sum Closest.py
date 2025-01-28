def threeSumClosest(nums, target):
    nums.sort()  # Sorting the array first
    closest_sum = float('inf')

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if abs(total - target) < abs(closest_sum - target):
                closest_sum = total

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return total  # The exact target sum found

    return closest_sum


# Example usage
nums = [-1, 2, 1, -4]
target = -100
print(threeSumClosest(nums, target))  # Output: 2
