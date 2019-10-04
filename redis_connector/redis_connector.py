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

# COMMON------------------------
    def keys(self, pattern):
        return self.client.keys(pattern)

    def is_exists(self, key):
        return self.client.exists(key)

# STRING-----------------------------
    def set(self, key, value):
        result = self.client.set(key, value)
        print " [ Redis Set ] key : ", key, " ; value :", value, " --- OK "
        return result

    def get(self, key):
        value = self.client.get(key)
        print "  [ Redis Get ] key : ", key, " ; value :", value, " --- OK "
        return value

# HASH--------------------------
    def hash_set(self, key, field, value):
        result = self.client.hset(key, field, value)
        return result

    def hash_get(self, key, field):
        value = self.client.hget(key, field)
        return value

# LIST----------------------------
    def list_push(self, key, value):
        result = self.client.lpush(key, value)
        return result

    def list_pop(self, key):
        value = self.client.lpop(key)
        return value

# SET----------------------------
    def set_add(self, key, value):
        result = self.client.sadd(key, value)
        return result

    def set_remove(self, key, value):
        value_result = self.client.srem(key, value)
        return value_result
# ZSET-----------------------------
    def zset_add(self, key, value, score):
        result = self.client.zadd(key, value, score)
        return result
