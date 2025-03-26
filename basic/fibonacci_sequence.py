a=1
b=0
x=int(input("Enter no of times to continue the sequence: "))
c=0
for i in range(x):
    print(c)
    c=a+b
    a=b
    b=c
