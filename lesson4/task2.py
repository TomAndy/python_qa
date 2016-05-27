
import json
from pprint import pprint

filename='bugs.json'
new_filename='bugs_new.json'


def main():
    with open(filename) as data_file:
        data = json.load(data_file)

    for aaa in data:
        aaa['Owner']='qa5'
    with open(new_filename,'w') as new_f:
        new_f.write(json.dumps(data))

if __name__ == '__main__':
    main()