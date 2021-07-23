# sort the array having only 0,1,2 in O(n) time and O(1) space.

def sortColors(nums):
    l = mid = 0; u = len(nums) - 1
    while mid <= u:
        if nums[mid] == 0:
            if nums[l] != 0:
                nums[mid],nums[l] = nums[l],nums[mid]
            else: mid += 1
            l += 1
            continue
        if nums[mid] == 2:
            if nums[u] != 2:
                nums[mid],nums[u] = nums[u],nums[mid]
            u -= 1
            continue
        if nums[mid] == 1: mid += 1
    return nums
nums = list(map(int,input().split()))
print(sortColors(nums))