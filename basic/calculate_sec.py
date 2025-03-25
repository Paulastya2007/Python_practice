# write a python program that calculates and print no of secords in a given year

# no of days * 24 * 60 * 60

def no_of_sec(n):
    print( n* 24 * 60 * 60)

def leap_year(n):
    b=False
    if n%100 ==0 and n%400==0:
        b=True
    elif n%4==0 and n%100!=0:
        b=True
    if b:
        no_of_sec(n+1)
    else:
        no_of_sec(n)

x=int(input("Enter year\t"))
leap_year(x)