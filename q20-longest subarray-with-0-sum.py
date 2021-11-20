# its a follow up question of Geeksforgeeks subarray with 0 sum

# The brute force soultion will be finding all the subarray with 0 sum and then calculate the max length
# Optimal solution: O(n)

class Solution:
    def maxLen(self, n, arr):
        dic = {}
        sm = maxi = 0
        for i in range(n):
            sm += arr[i]
            if not sm: maxi = i+1
            if sm in dic:
                maxi = max(maxi, i-dic[sm])
            else: dic[sm] = i
        return maxi