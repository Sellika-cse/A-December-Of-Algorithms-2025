l=[]
n=int(input())
for i in range(1,n):
    x=i*i
    if x in range(n):
        l.append(x)

print(*l)
print(len(l))
