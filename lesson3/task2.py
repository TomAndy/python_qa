
def func1():
    n=0
    f=open('/home/and/hometasks_python/python-for-qa-master/3-python-intermediate/alice_in_wonderland.txt','r')
    for line in f:
        if line.__contains__('. '):
            n=n+1
        if line.__contains__('.\n'):
            n = n + 1
        if line.__contains__('... '):
            n=n+1
        if line.__contains__('...\n'):
            n = n + 1
        if line.__contains__('.\''):
            n = n + 1
        if line.__contains__('? '):
            n = n + 1
        if line.__contains__('! '):
            n = n + 1
        if line.__contains__('?\n'):
            n = n + 1
        if line.__contains__('!\n'):
            n = n + 1
    f.close()
    print(n)

if __name__== '__main__':
    func1()
