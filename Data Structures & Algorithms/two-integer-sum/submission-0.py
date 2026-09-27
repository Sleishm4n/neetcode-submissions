class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = dict()

        for (index, value) in enumerate(nums):
            complement = target - value
            if complement in res:
                return [res[complement], index]
            else:
                res[value] = index