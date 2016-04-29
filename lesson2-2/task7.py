
def ispalindrome(str):
    if str[::]==str[-1::-1]:
        print ('Is palindrome')
    else:
        print ('Not palindrome')


if __name__== '__main__':
    str='rabar'
    ispalindrome(str)

