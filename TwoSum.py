class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = []
        for index in range(len(nums)):
            val = nums[index]
            complement = target - val
            if complement in nums and nums.index(complement) != index:
                ret.append(nums.index(complement))
                ret.append(index)
                break
        return ret
