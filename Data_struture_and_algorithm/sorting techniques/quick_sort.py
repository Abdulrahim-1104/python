def quicksort(arr,low,high):
    if low >= high:
        return 
    start = low
    end = high
    mid = (high+low)//2
    pivot = arr[mid]
    while start <= end:
        while arr[start] < pivot:
            start += 1

        while arr[end] > pivot:
            end -= 1

        if start <= end:
            arr[start],arr[end] = arr[end],arr[start]
            start += 1
            end -= 1
    quicksort(arr,low,end)
    quicksort(arr,start,high)

arr = [5,6,4,2,3,1]
quicksort(arr,0,len(arr)-1)
print(arr)