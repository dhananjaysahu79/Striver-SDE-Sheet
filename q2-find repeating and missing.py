# Approach 1: O(n) time and O(n) space

arr = list(map(int,input().split()))
s = [0] * len(arr)
for i in arr:
    s[i-1] += 1
r_num = num = 0
for i in range(len(arr)):
    if s[i] == 2: r_num = i + 1
    if s[i] == 0: num = i + 1
print(num,r_num)


# Approach 2: O(n) time and O(1) space
# In this approach we will traverse each element amd mark the index(that is equal to element - 1)
# to negative, Example suppose we got 5 then we will mark the value at index 4 as minus of that value.
# eg: 5 2 1 2 3
# when we get 5 then we will mark the value at index 4 as negative(Here in this case -3)
# After first iteration aray will be: 5 2 1 2 -3

arr = list(map(int,input().split()))
repeated_number = missing_number = 0
for i in range(len(arr)):
    if arr[abs(arr[i])-1] > 0:
        arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
    else: repeated_number = arr[i]
    print(arr)
for i in range(len(arr)):
    if arr[i] > 0: missing_number = i + 1
print(repeated_number,missing_number)