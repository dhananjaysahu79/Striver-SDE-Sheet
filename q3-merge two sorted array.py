# Merge two sorted array in O(1) space and O(nlogn + mlogm) time
# Difficulty level: Hard

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

a = len(arr1) - 1
b = 0

while a >= 0 and b < len(arr2):
    if arr2[b] < arr1[a]:
        arr2[b],arr1[a] = arr1[a],arr2[b]
        a -= 1
        b += 1
    else: break
arr1.sort()
arr2.sort()
print(*arr1,*arr2)