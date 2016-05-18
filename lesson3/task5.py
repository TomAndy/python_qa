import os


main_directory='/home/and/python-for-qa/'
directory='lesson'

def generate_file_tree():
    if not os.path.exists(main_directory):
        os.makedirs(main_directory)
    for i in range(1,9):
        if not os.path.exists(main_directory+directory+str(i)):
            os.makedirs(main_directory+directory+str(i))
            filepath=main_directory+directory+str(i)
            for j in range(1,7):
                filename=filepath+"/"+'task{}.py'.format(j)
                with open(filename, "w") as f:
                    f.close()


if __name__== '__main__':
    generate_file_tree()