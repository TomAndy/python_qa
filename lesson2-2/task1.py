

def concat(str):
    if len(str)<10:
        return None
    else:
        return str[:10]+str[-10::1]


if __name__ == '__main__':
    aa='abcdefghij'
    print (concat(aa))
