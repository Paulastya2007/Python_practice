a=[]
for i in range(int(input('Enter number of elements in the list\t'))):
    a.append(int(input('Enter number\t')))
b=a.copy()
b.remove(max(b))
print(f'2nd largest in here {a} is {max(b)}')