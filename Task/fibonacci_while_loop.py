##0 1 1 2 3 5 8 13 21 34 55 89
a=0
b=1
n=int(input("enter number:"))
print(a,end="")
while b<n:
    print(b,end="")
    a,b=b,a+b
