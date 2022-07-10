from classes import InputData
from main import DATA_DIR


def FileDescriptor(query: InputData, n=999999999999999999):
    with open(file=DATA_DIR + query.file_name, mode='r') as file:
        counter = 0
        while counter < n:
            line = next(file).strip('\n')
            yield line
            counter += 1
