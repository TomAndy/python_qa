
def create_dict(n=100):
    dd={}
    for i in range(2,n+1,2):
        dd[i]=i**2
    return dd


if __name__== '__main__':
    n=2
    print (create_dict())

    print (create_dict(n))