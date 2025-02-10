# using loops
def binarysearch_loop(arr,target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (end+start)//2
        if target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            return mid
    return -1
# using recursion
def binarysearch_recursion(arr,target,start,end):
    if start > end:
        return -1
    
    mid = (end+start)//2
    if target > arr[mid]:
        return binarysearch_recursion(arr,target,mid+1,end)
    elif target < arr[mid]:
        return binarysearch_recursion(arr,target,start,mid-1)
    else:
        return mid
def bs_2d(arr,target,start,end,col):
    if start > end:
        return -1
    if arr[col][len(arr[col])-1] < target and col < len(arr)-1:
        return bs_2d(array,target,start,len(arr[col+1])-1,col+1)
    mid = (end + start)//2
    if target > arr[col][mid]:
        return bs_2d(arr,target,mid+1,end,col)
    elif target < arr[col][mid]:
        return bs_2d(arr,target,start,mid-1,col)
    else:
        return '[{}][{}]'.format(col,mid)
arr = [1,2,3,4,5]
array = [[1,2,3],[4,5,6],[7,8,9]]
target = 4
print(binarysearch_loop(arr,target))
print(binarysearch_recursion(arr,target,0,len(arr)-1))
print(bs_2d(array,target,0,len(array[0])-1,0))