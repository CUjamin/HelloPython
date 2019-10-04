from utils.properties_utils.properties_utils import PropertiesUtils

if __name__ == '__main__':
    print "PATH:", ('__file__')
    properties_utils = PropertiesUtils('../../../config/config.properties')
    value = properties_utils.get_value('bool_value')
    print (value)
    value = properties_utils.get_value('int_value')
    print (value)
    value = properties_utils.get_value('str_value')
    print (value)
