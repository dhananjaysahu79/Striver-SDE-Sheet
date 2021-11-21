# O(n)
# Leetcode: 3 | medium

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi, count, n, dic = 0, 0, len(s), {}
        for i in range(n):
            curr_char = s[i]
            if curr_char in dic and count >= i - dic[curr_char]:
                count = i - dic[curr_char]
            else: count += 1
            dic[curr_char] = i
            maxi = max(maxi, count)
        return maxi