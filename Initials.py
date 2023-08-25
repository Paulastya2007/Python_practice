a=input('Enter name\t').lower()+' '
f=0
ns=''
ind=0
for e in a:
    if e == ' ':
        temp=a[f:ind]
        ns=ns+temp[0].upper()+'.'
        f=ind+1
    ind+=1
print(ns)
