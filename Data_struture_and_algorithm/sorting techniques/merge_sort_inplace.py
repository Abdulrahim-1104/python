
def merge(arr,start,mid,end):
    join = list()
    i,j = start,mid

    while i < mid and j < end:
        if arr[i] < arr[j]:
            join.append(arr[i])
            i += 1
        else:
            join.append(arr[j])
            j += 1
    while i < mid:
        join.append(arr[i])
        i += 1
    while j < end:
        join.append(arr[j])
        j += 1

    for k in range(len(join)):
        arr[k+start] = join[k]


def mergesort(arr,start,end):
    if end - start == 1:
        return
    mid = (end + start)//2

    # dividing
    mergesort(arr,start,mid)
    mergesort(arr,mid,end)

    #merging
    merge(arr,start,mid,end)

arr = [5,6,4,2,3,1]
mergesort(arr,0,len(arr))
print(arr)