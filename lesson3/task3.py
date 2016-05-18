
# Write a script to convert strings to date objects. Input list:
#
#         11 Jan 2016
#         4 April 2011
#         11.03.2014
#         03/24/91
#
# Script should have defined supported dates formats. Conversion should be in the loop

from datetime import datetime
def func1():
    date_object=[]
    format_list=['%d %b %Y','%d %B %Y','%d.%m.%Y','%m/%d/%y']
    date_list=['11 Jan 2016','4 April 2011','11.03.2014','03/24/91']
    i=0
    for item in date_list:
        print(item)
        print(format_list[i])
        date_object.append(datetime.strptime(item,format_list[i]).date())
        i=i+1
    print(date_object)


if __name__== '__main__':
    func1()