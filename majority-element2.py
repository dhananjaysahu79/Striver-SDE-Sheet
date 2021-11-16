# Booyer Moore Voting Algorithm
# O(n) time and O(1) space


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        max1 = max2 = count1 = count2 = 0
        for i in nums:
            if i == max1: count1 += 1
            elif i == max2: count2 += 1
            elif count1 == 0:
                max1 = i
                count1 = 1
            elif count2 == 0:
                max2 = i
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = count2 = 0

        for i in nums:
            if i == max1: count1 += 1
            if i == max2: count2 += 1

        ans = []
        if count1 > len(nums) // 3: ans.append(max1)
        if max1 != max2 and count2 > len(nums) // 3: ans.append(max2)
        return ans


