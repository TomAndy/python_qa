import requests
from requests.auth import HTTPBasicAuth
import json

filename='clients.json'
ENDPOINT='https://python-for-qa.herokuapp.com/login'

def main():
    with open(filename) as data_file:
        data = json.load(data_file)

    i=1
    for aaa in data:
        response = requests.get(ENDPOINT, auth=HTTPBasicAuth(aaa['name'], aaa['password']))
        if response.status_code !=200:
            print(aaa['name'])


if __name__ == '__main__':
    main()