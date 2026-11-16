class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summ = {}

        for i, num in enumerate(nums):
            complement = target - num 
            if complement in summ:
                return [summ[complement], i]
            summ[num] = i
        
        return []

        