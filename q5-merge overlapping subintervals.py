def merge(nums):
    nums.sort()
    stack = [nums[0]]
    for i in nums[1:]:
        if i[0] <= stack[-1][1]:
            stack[-1][1] = max(i[1],stack[-1][1])
        else: stack.append(i)
    return stack

# arr = list(map(int,input().split()))
# nums = []
# for _ in range(0,len(arr),2):
#     nums.append([arr[_],arr[_+1]])
# print(merge(nums))
