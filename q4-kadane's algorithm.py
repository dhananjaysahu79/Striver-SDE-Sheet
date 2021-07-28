def maxSubArray(nums):
    s = 0; mx = nums[0]
    for i in nums:
        s += i
        mx = max(mx,s)
        if s < 0: s = 0
    return mx

print(maxSubArray(list(map(int,input().split()))))
