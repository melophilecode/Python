import random
def kth(arr,k):
    mini=[]
    for i in range(0,len(arr)):
        a=min(arr)
        arr.remove(a)
        mini.append(a)
    k=k-1
    print("Array After Sorting:",mini)
    print("Kth minimum number:",mini[k])
#Driver Code
arr=[96,28,21,104,304,10,8,20]
print("Given Array:",arr)
key=len(arr)
k=random.randint(1,key)
print("K value:",k)
kth(arr,k)

