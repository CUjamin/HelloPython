import logging


class FileOperator:
    def __init__(self):
        pass

    def print_file(self, file_name):
        logging.info(' [ open the file:', file_name, ' ] ')
        with open(file_name) as file_object:
            # for line in file_object:
            # print(line.rstrip())
            lines = file_object.readlines()
        for line in lines:
            logging.info(line.rstrip())
        logging.info(' [ end ] \n')

    def read_file(self, file_name):
        logging.info(' [ read the file:', file_name, ' ] ')
        with open(file_name) as file_object:
            contents = file_object.read()
        logging.info(' [ end ] \n')
        return contents

    def over_write_file(self, file_name, line):
        logging.info(' [ read the file:', file_name, 'over write ', line, ' ] ')
        self.write_file(file_name, line, 'w')
        logging.info(' [ end ] \n')

    def append_write_file(self, file_name, line):
        logging.info(' [ append_write_file : ', file_name, ' ; append : ', line, ' ] ')
        self.write_file(file_name, line, 'a')
        logging.info(' [ end ] \n')

    def write_file(self, file_name, line, write_type):
        with open(file_name, write_type) as file_object:
            file_object.write(line)
        pass
