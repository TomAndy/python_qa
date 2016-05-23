
import requests
import re

ENDPOINT = 'http://deshevshe.ua/photocleaning-dataflash/dataflash_df1817.html'

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


def main():

    response = requests.get(ENDPOINT)
    # print(response.text)
    dText = response.text.split()
    search_word = 'price'
    i=0
    for text_word in dText:
        if findWholeWord(search_word)(text_word):
            print(''.join(c for c in text_word if c.isdigit()))
            break
        i=i+1


if __name__ == '__main__':
    main()