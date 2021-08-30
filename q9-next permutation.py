class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        c = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                c = i
                break
        if c != -1:
            for i in range(len(nums)-1,-1,-1):
                if nums[i] > nums[c]:
                    nums[i],nums[c] = nums[c],nums[i]
                    break
        a = c+1
        b = len(nums) - 1
        while a < b:
            nums[a],nums[b] = nums[b],nums[a]
            a+=1
            b-=1