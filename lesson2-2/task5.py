
def sum13(list):
    summ=0
    for item in list:
        if not (isinstance(item,str) and isinstance(item,bool)):
            if item!=13:
                summ=summ+item
            else:
                break
    return summ


if __name__== '__main__':
    list=[1, 2, 2, 1, 13, 5, 4, 2]
    print (sum13(list))
