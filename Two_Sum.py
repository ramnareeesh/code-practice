# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution:
    def twoSum(self, nums, target):
        out_list = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if  i != j and nums[i] + nums[j] == target:
                    out_list.append([i, j])
        return out_list[0]

    # alternate method using hashmaps or dictionaries to achieve O(n)

    def twoSumDict(self, nums, target):
        num_dict = {}
        for i in range(len(nums)):
            num_dict[nums[i]] = i

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in num_dict and num_dict[difference] != i:
                return [i, num_dict[difference]]

sol = Solution()
nums = [2, 7, 11, 15]
target = 9
print(sol.twoSum(nums, target))
print(sol.twoSumDict(nums, target))
