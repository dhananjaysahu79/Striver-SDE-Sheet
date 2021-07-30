# Find the duplicate number in O(n) time and O(1) space.
# You can't manipulate the array either.

# Appraoch : Hare and Tortoise method

def findDuplicate(arr):
    slow = arr[arr[0]]; fast = arr[arr[arr[0]]]
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow

print(findDuplicate(list(map(int,input().split()))))