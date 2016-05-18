
def func1():
    ll=[i for i in range(1,10001) if not((i%2) or (i%3))]
    print(ll)

def func2():
#     filter(function, iterable) is equivalent to [item for item in iterable if function(item)]
    ll=filter(lambda x:not((x%2)or(x%3)),range(1,10001))
    print(ll)

if __name__== '__main__':
    func1()
    func2()