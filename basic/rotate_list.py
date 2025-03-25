''' write a program that rotates the elements of a list so that element of the 1st index moves to the second .......
and element of the last index moves to the first'''

s=[]
n=int(input("Enter no of elements to be inputed in the list\t"))
for i in range(n):
    s.append(input("Enter element\t"))

print(f"Original list {s}")

p=s[-1:]+s[:-1]
print(p)
