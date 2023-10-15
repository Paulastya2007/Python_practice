def loop(s,e):
    if s<=e:
        k=''
        if s%3==0:
            k+='Fizz'
        if s%5==0:
            k+='Buzz'
        print(s if k=='' else k)
        s+=1
        return loop(s,e)
    
loop(1,100)
    