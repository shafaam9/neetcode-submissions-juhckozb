class Solution:
    def isAlphaNumeric(self, c) -> bool:
        return c.isalnum()

    def isPalindrome(self, s: str) -> bool:
        leftPtr = 0
        rightPtr = len(s) - 1

        while leftPtr < rightPtr:
            while leftPtr < rightPtr and not self.isAlphaNumeric(s[leftPtr]):
                leftPtr += 1

            while rightPtr > leftPtr and not self.isAlphaNumeric(s[rightPtr]):
                rightPtr -= 1

            if s[leftPtr].lower() != s[rightPtr].lower():
                return False
            
            leftPtr += 1
            rightPtr -= 1

        return True
    
        