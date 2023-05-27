def rec(x,s):
    if x>0:
        s+=(x%10)**3
        x=x//10
        return rec(x,s)    
    else:
        return s


a=int(input('Enter number to be checked\t'))
print("Armstrong Number " if rec(a,0)==a else 'Not Armstrong Number')