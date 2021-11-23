# Here list taken because of we need comma between two numbers otherwise we can solve it by using only one for loop
a = int(input())
b=[]
for i in range(1,a*2):
    if i%2!=0:
        b.append(i)
    i+=1
d=",".join(map(str,b))
print(d)
