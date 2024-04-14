def vowl(k):
    a=k.lower()
    if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
        return True
    return False

open_file=open('/workspaces/Python_practice/FileHandeling/poem.txt','r')
s=open_file.readlines()
num=0
for i in s:
    for j in i:
        if vowl(j):
            num+=1
print(num)