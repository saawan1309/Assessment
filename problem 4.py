a=list(map(int,input().split()))
b=[]
c=0
for i in range(1,10):
    for j in a:
        if j%i==0:
            c+=1
        j+=1
    b.append(c)
    c=0
    i+=1
for i in range(1,10):
    print(f"{i}:{b[i-1]}",end=" ")

