
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

list4=[]
list4.extend(list1)
list4.extend(list2)
list4.extend(list3)
print list4
print list4[-1:-len(list4)-1:-1]
