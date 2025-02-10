def selectionsort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]

arr = [3,4,2,5,1]
selectionsort(arr)
print(arr)
