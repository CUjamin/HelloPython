import re
def find_start_with(file_name):
    f = open(file_name)
    for line in f:
        if line.startswith('cuj'):
            print line.rstrip()


def find_end_with(file_name):
    f = open(file_name)
    for line in f:
        if line[:-1].endswith('Java'):
            print line.rstrip()


#find_start_with('regular.txt')
#find_end_with('regular.txt')