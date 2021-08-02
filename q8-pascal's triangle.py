# print the triangle till the given row.
def generate(numRows):
    ans = []
    for i in range(1,numRows+1):
        if i == 1: ans.append([1])
        elif i == 2: ans.append([1,1])
        else:
            temp = [1]
            for j in range(i-2):
                temp.append(ans[i-2][j]+ans[i-2][j+1])
            temp.append(1)
            ans.append(temp)
    return ans
print(generate(int(input())))

# There can be two variation that can be asked in interviews:
# 1: Print the number at rth row and cth column:
#    for that we can use the following formula:
#        (r-1) C (c-1) in O(n)

def generate(r,c):
    prev = 1;
    for i in range(1,c+1):
        prev = (prev * (r - i + 1)) // i
    return prev
r,c = map(int,input().split())
print(generate(r,c))



# 2: Print the entire rth row:
#    for that we can interate i through 0 to r-1,
#    and then append  r C i which can be calculated in O(1) time using the
#    formula rci = rC(i-1) * (r - i + 1) / i
#    so the first element of the row will be rC0 that is 1 and using this
#    mathematical formula we can easily find rest of the elements in total of O(r)

def generate(r):
    prev = 1;
    ans = [1]
    for i in range(1,r+1):
        prev = (prev * (r - i + 1)) // i
        ans.append(prev)
    return ans
print(*generate(int(input())))

