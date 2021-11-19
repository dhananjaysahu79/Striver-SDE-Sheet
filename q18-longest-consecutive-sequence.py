# O(n)
# leetcode 128 | Medium

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxi = 0
        for i in s:
            if i-1 in s: continue
            curr = i + 1; count = 1
            while curr in s:
                count += 1; curr += 1
            maxi = max(maxi, count)
        return maxi