def merge(left,right):
    l,r,j = 0,0,0
    join = list()
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            join.append(left[l])
            j += 1
            l += 1
        else:
            join.append(right[r])
            j += 1
            r += 1
    while l < len(left):
        join.append(left[l])
        j += 1
        l += 1
    while r < len(right):
        join.append(right[r])
        j += 1
        r += 1
    return join
def mergesort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left,right)

arr = [5,6,45,6,4,3,3,5,6,7,2,3,1]
print(mergesort(arr))