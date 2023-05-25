def insert(arr):
    for i in range(len(arr)):
        tmp=arr[i]
        j=i-1
        while j>=0 and tmp<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=tmp
    return arr
arr=[799,12,31,25,8,32,17]
print('Before Sorting:',arr)
ar=insert(arr)
print('After Sorting:',ar)
