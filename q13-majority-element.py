# Naive easiest O(n) space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
            if dic[i] > n/2: return i
