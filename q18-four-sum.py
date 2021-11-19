# O(NNN)
# leetcode 18 | Medium

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for a in range(n-3):
            if a and nums[a] == nums[a-1]: continue
            for b in range(a+1,n-2):
                if b > a + 1 and nums[b] == nums[b-1]: continue
                c = b + 1; d = n - 1
                while c < d:
                    sm = nums[a] + nums[b] + nums[c] + nums[d]
                    if sm == target:
                        ans.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        while c < d and nums[c] == nums[c-1]: c += 1
                    elif sm > target: d -= 1
                    else: c += 1
        return ans