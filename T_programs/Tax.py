def prints(pan,name,taxinc,taxp):
    print('PAN\tNAME\tTAXABLE-INCOME\tTAX')
    print(f'{pan}\t{name}\t{taxinc}\t{taxp}')

a=int(input('Enter PAN number\t'))
n=input('Enter name\t')
inc=int(input('Enter taxable income\t'))
if inc<=100000:
    prints(a,n,inc,'No tax')
elif 100001<=inc and inc>=150000:
    prints(a,n,inc,((inc-100000)*10)/100)
elif 150001<=inc and inc>=250000:
    prints(a,n,inc,(((inc-150000)*20)/100)+5000)
else:
    prints(a,n,inc,(((inc-250000)*30)/100)+25000)
