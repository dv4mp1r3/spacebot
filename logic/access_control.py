class AccessControlMeta(type):

    def __instancecheck__(self, instance):
        return self.__subclasscheck__(type(instance))

    def __subclasscheck__(self, subclass):
        return (hasattr(subclass, 'allow_access') and
                callable(subclass.allow_access))


class AccessControlInterface(metaclass=AccessControlMeta):
    pass


class DebugAlwaysAllowAccessControl(AccessControlInterface):

    @classmethod
    def allow_access(cls, user_id: int) -> bool:
        return True
