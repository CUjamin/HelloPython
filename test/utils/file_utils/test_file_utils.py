from utils.file_utils.file_operator import FileOperator
import unittest


class FileOperatorTest(unittest.TestCase):
    def test_read_file(self):
        print '---------------------------------------test_read_file------------------------------------------------'
        file_path = '../../../config/config.properties'
        file_operator = FileOperator()
        content = file_operator.read_file(file_path)
        print content

    def test_print_file(self):
        print '---------------------------------------test_print_file------------------------------------------------'
        file_path = '../../../config/config.properties'
        file_operator = FileOperator()
        file_operator.print_file(file_path)

    def test_write_file(self):
        print '---------------------------------------test_write_file------------------------------------------------'
        file_path = '../../../config/config.properties'
        file_operator = FileOperator()
        file_operator.append_write_file(file_path, 'hhhhhhhhhhh')

unittest.main()
