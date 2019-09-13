class PropertiesUtils():
    file
    def __init__(self,file_name):
        file = open(file_name)
        for line in file:
            print (line.rstrip())

    def get_value(self,key):
        return file


if __name__ == '__main__':
    propertiesutils = PropertiesUtils('config.properties')
    value = propertiesutils.get_value("")
    print (value)