class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []

        i = 0
        while i < len(nums):
            correct_idx = nums[i] - 1 
            if nums[i] != nums[correct_idx]:
                #swap
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1
        
        print(nums)
        for i in range(len(nums)):
            if i != nums[i] - 1:
                res.append(i + 1)
        return res

