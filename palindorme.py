k=input('Enter word\t')
if k==k[::-1]:
    print(f'Given word is palindrome {k}')
else:
    print(f'Given word is not palindrome {k}')