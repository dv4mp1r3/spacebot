from logic.data_providers import CsvDataSource


class AccessControlMeta(type):

    def __instancecheck__(self, instance):
        return self.__subclasscheck__(type(instance))

    def __subclasscheck__(self, subclass):
        return (hasattr(subclass, 'allow_access') and
                callable(subclass.allow_access))


class AccessControlInterface(metaclass=AccessControlMeta):
    pass


class TelegramCsvBasedAccessControl(AccessControlInterface):
    _data_source = None

    def __new__(cls, data_source: CsvDataSource,  *args, **kwargs):
        cls._data_source = data_source
        return cls

    @classmethod
    def allow_access(cls, user_id: int) -> bool:
        for row in cls._data_source.get_records():
            try:
                if int(row[0]) == user_id:
                    return True
            except ValueError:
                continue
        return False
    