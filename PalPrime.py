def isPrime(n):
    k=0
    for i in range(1,n+1):
        if n%i==0:
            k+=1
    return k==2

def isPalindrome(n):
    k=n
    ps=0
    while (k>0):
        temp=k%10
        k//=10
        ps=(ps*10)+temp
    return n==ps


lower=int(input('Enter lower range\t'))
upper=int(input('Enter upper range\t'))
for i in range(lower,upper+1):
    if isPalindrome(i) and isPrime(i):
        print(i)