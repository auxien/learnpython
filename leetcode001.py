from typing import List

#nums = [2,7,11,15], target = 9
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i <= len(nums) - 2:
            j = 0
            while i+j <= len(nums) - 2:
                if nums[i] + nums[i + j + 1] == target:
                    return [i, i + j + 1]
                j += 1
            i += 1


nums = [3, 5, 1, 8]
target = 6
m = Solution()
print(m.twoSum(nums, target))





