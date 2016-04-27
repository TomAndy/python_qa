# print 'Write a program to calculate the number of times that the string \'hi\' appears anywhere in the given string ' \
#       'and change \'hi\' to \'bye\'. Case should be ignored'

import re

str1='hI. Today is Hi again. I can\'t stand using hi in any string'

x=str1.upper().count("hi".upper())
print x
str2=str1.replace('hi','bye').replace('Hi','bye').replace('HI','bye').replace('hI','bye')
print str2

insens_str=re.compile(re.escape('hi'),re.IGNORECASE)
print insens_str.sub('bye',str1)