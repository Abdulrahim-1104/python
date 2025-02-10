def bubblesort(arr):
    for i in range(1,len(arr)):
        for j in range(len(arr)-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

arr = [3,4,2,5,1]
bubblesort(arr)
print(arr)