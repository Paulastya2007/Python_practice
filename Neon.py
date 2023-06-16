a=int(input("Enter number\t"))
b=a**2
c=b
d=0
while c>0:
    d+=c%10
    c//=10
print(f'Yes {a} is a neon number ' if d==a else f'No {a} is not a neon number ')