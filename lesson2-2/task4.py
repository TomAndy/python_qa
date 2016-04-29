

def evaluate():
    for a in (True,False):
        for b in (True,False):
            for c in (True, False):
                print ('\na={}, b={}, c={}'.format(a,b,c))
                print ('res={}'.format((a or not b) and (c or not a)))


if __name__== '__main__':
    evaluate()
