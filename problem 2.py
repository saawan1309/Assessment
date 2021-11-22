a = int(input())
b=[]
for i in range(1,a*2):
    if i%2!=0:
        b.append(i)
    i+=1
d=",".join(map(str,b))
print(d)