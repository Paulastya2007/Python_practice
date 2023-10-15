def loop(e):
    for i in range(1,e+1):
        k=''
        if i%3==0:
            k+='Fizz'
        if i%5==0:
            k+='Buzz'
        print(i if k=='' else k)

loop(100)