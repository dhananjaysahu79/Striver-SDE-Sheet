# Interviewbit | Medium
# Solution 1: Naive Brute force approach
# SImply  find all the subarrays and check
# O(NN) solution


class Solution:
    def solve(self, A, B):
        count = 0
        n = len(A)
        for i in range(n):
            xors = 0
            for j in range(i,n):
                xors ^= A[j]
                if xors == B: count += 1
        return count

# Solution 2: O(n)
# take a dicionary and store all the prefix xors sum while travesrsing
# check the required prefix xorsums to make it equal to k exist or not or how many times it exist.
# add it to tyhe count variable

class Solution:
    def solve(self, A, B):
        count = xors = 0
        n = len(A)
        dic = {}

        for num in A:
            xors ^= num
            if xors == B: count += 1
            prefix_xor = xors ^ B
            if prefix_xor in dic: count += dic[prefix_xor]
            if xors in dic: dic[xors] += 1
            else: dic[xors] = 1

        return count