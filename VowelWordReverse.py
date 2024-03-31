def vlw(n):
    #takes in a word
    a=['a','e','i','o','u','A','E','I','O','U']
    if n[0] in a:
        return n[::-1]
    else:
        return n
    
n=input('Enter string\t')
k=n.split()
word=''
for i in k:
    word=word+vlw(i)+' '
print(word)

