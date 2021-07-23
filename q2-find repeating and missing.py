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
