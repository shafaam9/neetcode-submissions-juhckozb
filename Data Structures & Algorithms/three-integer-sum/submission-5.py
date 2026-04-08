class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        goal = 0
        nums = sorted(nums)
        res = []
        j = 1 if len(nums) > 1 else 0
        k = len(nums) - 1

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < goal:
                    j += 1
                elif total > goal:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    
                    j += 1
                    k -= 1

                    while j < len(nums) - 1 and nums[j] == nums[j - 1]:
                        j += 1
                    while k > 0 and nums[k] == nums[k + 1]:
                        k -= 1

        return res
            
