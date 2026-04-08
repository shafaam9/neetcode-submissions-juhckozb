class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start = 0
        max_len = 0
        letter_freq = {}

        for window_end in range(len(s)):
            letter_freq[s[window_end]] = letter_freq.get(s[window_end], 0) + 1

            while letter_freq[s[window_end]] > 1:
                letter_freq[s[window_start]] -= 1
                window_start += 1
            
            max_len = max(max_len, window_end - window_start + 1)
        return max_len 
        

        