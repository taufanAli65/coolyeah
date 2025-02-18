def selectionSort(arr):
    for i in range(len(arr)-1):
        index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[index]:
                index = j
        elemen = arr[index]
        arr[index] = arr[i]
        arr[i] = elemen
    return arr

def search(arr, target):
    selectionSort(arr)
    for i in range (len(arr)) :
        if target == arr[i] :
            return i+1