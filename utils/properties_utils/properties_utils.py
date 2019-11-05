import logging


class PropertiesUtils:
    # file
    config_map = {}

    def __init__(self, file_name):
        self.file = open(file_name)
        for line in self.file:
            if line.startswith('['):
                continue
            else:
                key_value = line.split(':')
                self.config_map[key_value[0]] = key_value[1].rstrip()
        logging.info(" file name : ", file_name, "\n config : ", self.config_map)

    def get_value(self, key):
        return self.config_map.get(key)
