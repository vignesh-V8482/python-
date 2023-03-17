def is_armstrong(num):
    num_digits=len(str(num))
    sum_of_digits=sum(int(digit)**num_digits for digit in str(num))
    if sum_of_digits==num:
        return True
    else:
        return False
N=int(input("enter the size of the list:"))
lst=[]
for i in range(N):
    lst.append(int(input("enter a number:")))
for i in range(len(lst)):
    if is_armstrong(lst[i]):
        lst[i]=1
    else:
        lst[i]=0
print("updated list:",lst)
