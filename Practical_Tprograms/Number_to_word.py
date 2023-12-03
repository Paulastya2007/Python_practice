words={
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    0:'zero'
}
num=int(input('Enter numerical value\t'))
s=num
word=''
while s>0:
    temp=s%10
    word=words[temp]+' '+word
    s=s//10

print(f'Number in words {num} is {word}')

