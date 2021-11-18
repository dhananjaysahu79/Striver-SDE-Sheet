# O(NlogN) Solution
# space compexity: O(n)
# leetcode: 493 | Hard

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0

        def mergeSort(nums):
            if len(nums) < 2: return nums
            mid = len(nums) // 2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])

            # finding pair
            a = b = 0
            while a < len(left) and b < len(right):
                if left[a] > 2 * right[b]:
                    self.count += (len(left) - a)
                    b += 1
                else:
                    a += 1

            a = b = 0
            arr = []
            # merging the sorted arrays
            while a < len(left) or b < len(right):
                if a < len(left) and (b >= len(right) or left[a] < right[b]):
                    arr.append(left[a])
                    a += 1
                else:
                    arr.append(right[b])
                    b += 1
            return arr

        arr = mergeSort(nums)
        return self.count


