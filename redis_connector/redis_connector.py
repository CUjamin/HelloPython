from redis import StrictRedis, client


class RedisConnector:
    host = '127.0.0.1'
    port = 6379
    server_name = 'mymaster'
    db = 0
    client

    def __init__(self, host, port, server_name, db):
        self.host = host
        self.port = port
        self.server_name = server_name
        self.db = db
        print " [ Start connect redis ... ... ] host: ", host, " port: ", port, " ;server_name: ", server_name, " ;db: ", db
        self.client = StrictRedis(self.host, self.port, self.db)
        print " [ Start connect redis --- OK  ] "
        pass

    def set(self, key, value):
        result = self.client.set(key, value)
        print " [ Redis Set ] key : ", key, " ; value :", value, " --- OK "
        return result

    def get(self, key):
        value = self.client.get(key)
        print "  [ Redis Get ] key : ", key, " ; value :", value, " --- OK "
        return value
