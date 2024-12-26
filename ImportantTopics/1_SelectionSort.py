def selectionSort(arr: list[int]) -> list[int]:
    if len(arr)<=1:
        return arr
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[minIndex]:
                minIndex=j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

arr = [3,1325,82,5,92,35,24]
sortedArr = selectionSort(arr)
print(sortedArr)