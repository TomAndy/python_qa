
import requests
from requests.auth import HTTPBasicAuth



ENDPOINT = 'https://python-for-qa.herokuapp.com/data'
ENDPOINTGETTOKEN = 'https://python-for-qa.herokuapp.com/login'
USER = 'admin'
PASSWORD = 'password'

def main():
    response = requests.get(ENDPOINTGETTOKEN, auth=HTTPBasicAuth(USER,PASSWORD))

    received_resp = response.json()

    header_json = {'X-AUTH-TOKEN': received_resp['token'],
              'Accept': 'application/json'}

    response_json = requests.get(ENDPOINT, headers=header_json)
    # print(response_json.status_code)
    # print(response_json.headers)
    # print(response_json.text)
    # print('==============================================')

    header_xml = {'X-AUTH-TOKEN': received_resp['token'],
                   'Accept': 'application/xml'}


    response_xml = requests.get(ENDPOINT, headers=header_xml)
    # print(response_xml.status_code)
    # print(response_xml.headers)
    # print(response_xml.text)

    with open('file_json', "w") as f:
        f.write(response_json.text)
        f.close()



if __name__ == '__main__':
    main()