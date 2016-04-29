
def last_element(str):
    list = str.split(",")
    print (list[-1])



if __name__== '__main__':
    aa='abc def ghijklmnopq r'
    last_element(aa)

    bb='abc, def, dd, ff:edewfd ,e'
    last_element(bb)