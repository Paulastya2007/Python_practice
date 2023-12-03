digit_words ={
    '0':'zero',
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine'
}

num=int(input('Enter a number'))
num_str=str(num)
words=''
for k in num_str:
    words=words+digit_words[k]+' '
    

print(num, 'is',words)