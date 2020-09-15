#io_utilities.py
filepath= './data/iris.data'

def read_vanilla(filepath):
    with open(filepath,'r') as fp:
        data=fp.read()

    data_lines = data.split('\n')
    data_final= []


    for line in data_lines:
        data_final.append(line.split(','))

    data_final= [f.split(',') for f in data_lines]
    return data_final

print(read_vanilla(filepath))
