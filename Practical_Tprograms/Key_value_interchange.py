x={}
for i in range(int(input("Enter number of times\t"))):
    tk=input('Enter key\t')
    vk=input('Enter values\t')
    x[tk]=vk
print('Normal list\t',x)
inverted={}
for i in x:
    temp=x[i]
    if temp not in inverted:
        inverted[temp] = i


print('Inverted Dictionary\t',inverted)