class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPtr = 0 
        rightPtr = len(numbers) - 1

        while leftPtr < rightPtr:
            total = numbers[leftPtr] + numbers[rightPtr]
            if target > total:
                leftPtr += 1
            elif target < total:
                rightPtr -= 1
            else:
                return [leftPtr + 1, rightPtr + 1]
        return []
