class FileReader:
    def read_file(self, file_name):
        print('start------------------')
        with open(file_name) as file:
            for line in file:
                print(line.rstrip())
        print('end------------------')
