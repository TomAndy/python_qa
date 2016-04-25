# print 'Write a program to calculate the number of times that the string \'hi\' appears anywhere in the given string ' \
#       'and change \'hi\' to \'bye\'. Case should be ignored'

str1='hi. Today is hi again. I can\'t stand using hi in any string'

x=str1.count('hi')
print x
str2=str1.replace('hi','bye')
print str2