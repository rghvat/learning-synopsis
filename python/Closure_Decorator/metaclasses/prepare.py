# file: pepare.py

"""Using `__prepare__` to preserve definition order of attributes.

Needs Python 3.
"""


class AttributeOrderDict(dict):
    """Dict-like object used for recording attribute definition order.
    """

    def __init__(self, no_special_methods=True, no_callables=True):
        self.member_order = []
        self.no_special_methods = no_special_methods
        self.no_callables = no_callables
        super().__init__()

    def __setitem__(self, key, value):
        skip = False
        # Don't allow setting more than once.
        if key in self:
            raise AttributeError(
                'Attribute {} defined more than once.'.format(key))
        # Skip callables if not wanted.
        if self.no_callables:
            if callable(value):
                skip = True
        # Skip special methods if not wanted.
        if self.no_special_methods:
            if key.startswith('__') and key.endswith('__'):
                skip = True
        if not skip:
            self.member_order.append(key)
        super().__setitem__(key, value)


class OrderedMeta(type):
    """Meta class that helps to record attribute definition order.
    """

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        return AttributeOrderDict(**kwargs)

    def __new__(mcs, name, bases, cdict, **kwargs):
        cls = type.__new__(mcs, name, bases, cdict)
        cls.member_order = cdict.member_order
        cls._closed = True
        return cls

    # Needed to use up kwargs.
    def __init__(cls, name, bases, cdict, **kwargs):
        super().__init__(name, bases, cdict)

    def __setattr__(cls, name, value):
        # Later attribute additions go through here.
        if getattr(cls, '_closed', False):
            raise AttributeError(
                'Cannot set attribute after class definition.')
        super().__setattr__(name, value)


if __name__ == '__main__':

    class MyClass(metaclass=OrderedMeta, no_callables=False):
        """Test class with extra attribute `member_order`.
        """
        attr1 = 1
        attr2 = 2

        def method1(self):
            pass

        def method2(self):
            pass

        attr3 = 3
        # attr3 = 3  # uncomment to trigger exception

    print(MyClass.member_order)
    # MyClass.attr4 = 4 # uncomment to trigger exception
