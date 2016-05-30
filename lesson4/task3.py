# Write a script to parse habraharb_all.xml and print each article's title, author and all categories.

import xml.etree.ElementTree as etree


def main():
    course_xml = etree.parse('habrahabr_all.xml')

    root = course_xml.getroot()  # <Element 'course' at 0x10afd48d0>
    # print(root)

    # for child in root:
    #     print(child)

    for titles in root.iter('title'):
        print('Title:')
        print('%%%%%%%%%%%%%%%%%%%')
        print(titles.text.strip())
        print('===================')
        print('Authors:')
        print('@@@@@@@@@@@@@@@@@@@@@@')
        for autor in root[0].iter('author'):
            print(autor.text.strip())
        print('---------------------------')
        print('Categories:')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        for categ in root[0].iter('category'):
            print(categ.text.strip())
        print('===================')

    # for authors in root.iter('author'):
    #     print(authors.text.strip())
    # print('------------------')
    #
    # for categories in root.iter('category'):
    #     print(categories.text.strip())


if __name__ == '__main__':
    main()