def countInversion(arr):
    if len(arr) < 2: return 0
    mid = len(arr) // 2
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    count = 0
    count += countInversion(arr1)
    count += countInversion(arr2)

    # merge the array in ascending and find the inversions
    a = b = 0
    temp = []
    while a < len(arr1) and b < len(arr2):
        if arr2[b] < arr1[a]:
            count += len(arr1) - a
            temp.append(arr2[b])
            b += 1
        else:
            temp.append(arr1[a])
            a += 1

    while a < len(arr1):
        temp.append(arr1[a])
        a += 1
    while b < len(arr2):
        temp.append(arr2[b])
        b += 1
    for i in range(len(temp)): arr[i] = temp[i]
    return count

arr = list(map(int, input().split()))
print(countInversion(arr))