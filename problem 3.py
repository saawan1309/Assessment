a = int(input())
if a%2==0:
    a= a-1
for i in range(1,a*2):
    if i%2!=0:
        print(i,end=" ")
    i+=1