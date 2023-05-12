import random
import time
import matplotlib.pyplot as plt
x=[]
y=[]
def linear(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1

for i in range(3):
    arrele=int(input("Enter The Length Of the Array Element:"))
    x.append(arrele)
    arr=[random.randint(0,100) for _ in range(arrele)]
    print(arr)
    key=int(input("Enter The Search element from above Array:"))
    start = time.perf_counter()
    linearind=linear(arr,key)
    end = time.perf_counter()
    print("The Search Key Is found index position:",linearind)
    ms = (end-start) * 10*6
    y.append(ms)
    print("Time For Required To Search:",ms)
plt.plot(x,y)
plt.title("Linear Search:")
plt.xlabel("n")
plt.ylabel('time(sec)')
plt.show()
