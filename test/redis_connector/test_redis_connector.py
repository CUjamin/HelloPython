from redis_connector.redis_connector import RedisConnector
from utils.properties_utils.properties_utils import PropertiesUtils

if __name__ == '__main__':
    propertiesUtils = PropertiesUtils('../../config/redis.properties')
    host = propertiesUtils.get_value('host')
    port = propertiesUtils.get_value('port')
    server_name = propertiesUtils.get_value("server_name")
    db = propertiesUtils.get_value('db')
    redis_connector = RedisConnector(host, port, server_name, db)
    result = redis_connector.set('testkey', 'testvalue')
    print result
    result = redis_connector.get('testkey')
    print result