class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        freq_map = {}
        window_start = 0

        for window_end in range(len(s)):
            freq_map[s[window_end]] = freq_map.get(s[window_end], 0) + 1
            max_key_count = max(freq_map.values())
            while (window_end - window_start + 1) - max_key_count > k and freq_map[s[window_start]] > 0:
                freq_map[s[window_start]] -= 1
                window_start += 1
            max_len = max(max_len, window_end - window_start + 1)
        return max_len
