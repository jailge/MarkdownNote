
import redis, time

class RedisOperation:
    def __init__(self, host, port, db=0, password=""):
        pool = redis.ConnectionPool(host=host, port=port, db=db, password=password)
        self._r = redis.Redis(connection_pool=pool)

    def set(self, key, value):
        self._r.set(key, value)
    


if __name__ == '__main__':
    pool = redis.ConnectionPool(host='10.10.8.140', port=6379, db=0, password='gmxxb80111!')
    r = redis.Redis(connection_pool=pool)
    print(r.eval("return redis.call('set', KEYS[1], 'bar')", 1, "foo"))
    print(r.set(name='k1', value='v1', nx=True, px=30000))
    print("{:*<10}等待{:*>10}s".format('k1', 5))
    time.sleep(5)
    print(r.pttl('k1'))
    # r.set(name='k1', value='v2', nx=True, px=30000)

    """
    参数说明
    第一个参数: Lua语言
    第二个参数: key值个数
    第三个参数开始: key值1、key值2...通过KEYS[1]、KEYS[2]...访问
    最后不是key值参数: arg1、arg2...通过ARGV[1]、ARGV[2]...访问
    """
    print(r.eval("if redis.call('get', KEYS[1])==ARGV[1] then return redis.call('del', KEYS[1]) else return 0 end",1, 'k1', 'v1'))
    