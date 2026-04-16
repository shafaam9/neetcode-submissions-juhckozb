class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        #len(nums) == 3
        while i < len(nums): #
            correct_idx = nums[i]
            if 0 <= nums[i] < len(nums) and nums[i] != nums[correct_idx]:
                #swap
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return i + 1
            