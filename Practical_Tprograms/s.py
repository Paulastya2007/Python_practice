#s=1+x+x^2+......x^n
x=int(input('Enter base\t'))
n=int(input("Enter number of times to go\t"))
ml=0
for i in range(n+1):
    ml+=x**i
print(ml)