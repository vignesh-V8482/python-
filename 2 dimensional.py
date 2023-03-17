n=int(input())
a=[]
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
    a.sort()
for i in range(n):
    for j in range(n-1,-1,-1):
        print(a[i][j],end=" ")
    print()
