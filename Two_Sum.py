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

