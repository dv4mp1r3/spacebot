class DataCacheMeta(type):

    def __instancecheck__(self, instance):
        return self.__subclasscheck__(type(instance))

    def __subclasscheck__(self, subclass):
        return (hasattr(subclass, 'get_data') and
                callable(subclass.get_data) and
                hasattr(subclass, 'set_data') and
                callable(subclass.set_data))


class DataCacheInterface(metaclass=DataCacheMeta):
    pass


class UnlimitedTimeDataCache(DataCacheInterface):
    _cache = dict()

    @classmethod
    def gen_key(cls, command: str, username: str) -> str:
        return f'{command}-{username}'

    @classmethod
    def get_data(cls, key: str) -> str:
        if key in cls._cache:
            return cls._cache[key]
        return ''

    @classmethod
    def set_data(cls, key: str, data: str):
        cls._cache.update({key: data})


class UnlimitedTimeAnswersDataCache(UnlimitedTimeDataCache):
    @classmethod
    def gen_key(cls, command: str, username: str) -> str:
        return f'{command}-{username}'
