#A=p(1+r/100)**t    CI=A-P
p=int(input('Enter Principal amount\t'))
r=(int(input("Enter rate of interest\t")))/100
t=(int(input('Enter time in years\t')))
a=p*((1+r)**t)
print(f'Required Compound interest {a-p}')