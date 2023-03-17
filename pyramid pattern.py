n=5
for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(" ",end="")
        for j in range(1,2*i):
            if i%2==0:
                print("#",end=" ")
            else:
                print("*",end=" ")
        print()
