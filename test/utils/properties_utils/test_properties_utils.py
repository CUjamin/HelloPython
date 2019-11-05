from utils.properties_utils.properties_utils import PropertiesUtils
import unittest


class PropertiesUtilsTest(unittest.TestCase):
    def test_get_value(self):
        print "PATH:", ('__file__')
        properties_utils = PropertiesUtils('../../../config/config.properties')
        value = properties_utils.get_value('bool_value')
        self.assertEqual('true', value)
        value = properties_utils.get_value('int_value')
        self.assertEqual('1', value)
        value = properties_utils.get_value('str_value')
        self.assertEqual('test', value)


unittest.main()
