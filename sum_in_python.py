n = 4000000
x=[]
y=[]
sum=0

i, j = 0, 1
for i in range(n+1):
    i,j = j, j+i
    x.append(i)
    
for j in x:
    if j%2==0:
        y.append(j)
        sum += j


print(sum)
