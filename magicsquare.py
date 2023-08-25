def magic(n):
    print("Study The Rule First Then start Program")
    magic=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
            '''l.append(j) is one of mistake'''
        magic.append(l)
    
    
    i=n//2
    j=n-1
    count=n*n
    sum=int((n*(n**2 +1))/2)
    print("Sum Of The Matrix:",sum)
    ini=1
    while(count>=ini):
        if(i==-1 and j==n):
            i=0
            j=n-2
        if(i==-1):
            i=n-1
        if(j==n):
            j=n-n
        
        if(magic[i][j]!=0):
            i=i+1
            j=j-2
        else:
            magic[i][j]=ini
            ini=ini+1
            i=i-1
            j=j+1
    for i in range(n):
        for j in range(n):
            print(magic[i][j],end=" ")
        print()
print("Magic Square Is only For Odd Numbers")
n=int(input("Enter Square Matrix Size:"))
magic(n)

    
        
