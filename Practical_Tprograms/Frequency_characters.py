freq={}
tst_word=input('Enter a word to be tested\t')
for i in tst_word:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)