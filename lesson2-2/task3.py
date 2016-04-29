

def remove_dupl(list):
    new_list = []
    for item in list:
        if list.count(item)==1:
            new_list.append(item)
        else:
            pass
    print (new_list)


if __name__== '__main__':
    ll = [1, 2, 3, 4, 4, 6, 2]
    print (ll)
    remove_dupl(ll)
