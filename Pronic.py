a=int(input('Enter number to be checked\t'))
m=False
for i in range(a):
    if i * (i+1)==a:
        m=True
        break
if not m:
    print("Not pronic number\t",a)
else:
    print("Pronic number\t",a)