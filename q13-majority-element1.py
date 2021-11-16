# Naive easiest O(n) space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
            if dic[i] > n/2: return i


# Approach 2: O(1) space
# O(NlogN) time

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count = maxi = 1
        max_num = nums[0]

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                count += 1
            else: count = 1
            if count > maxi:
                max_num = nums[i]
                maxi = count
        return max_num

# O(n) time and O(1) space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = nums[0]
        count = 1
        for i in nums[1:]:
            if i == curr: count += 1
            else: count -= 1
            if not count:
                curr = i
                count = 1
        return curr