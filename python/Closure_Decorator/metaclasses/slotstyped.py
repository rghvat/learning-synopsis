# file: slotstyped.py

"""Use of descriptor and metaclass to get slots with
given types.
"""

from __future__ import print_function

class TypDescriptor(object):
    """Descriptor with type.
    """

    def __init__(self, data_type, default_value=None):
        self.name = None
        self._internal_name = None
        self.data_type = data_type
        if default_value:
            self.default_value = default_value
        else:
            self.default_value = data_type()

    def __get__(self, instance, cls):
        return getattr(instance, self._internal_name, self.default_value)

    def __set__(self, instance, value):
        if not isinstance(value, self.data_type):
            raise TypeError('Required data type is %s. Got %s' % (
            self.data_type, type(value)))
        setattr(instance, self._internal_name, value)

    def __delete__(self, instance):
        raise AttributeError('Cannot delete %r' % instance)


class TypeProtected(type):
    """Metaclass to save descriptor values in slots.
    """

    def __new__(mcl, name, bases, cdict):
        slots = []
        for attr, value in cdict.items():
            if isinstance(value, TypDescriptor):
                value.name = attr
                value._internal_name = '_' + attr
                slots.append(value._internal_name)
        cdict['__slots__'] = slots
        return super(TypeProtected, mcl).__new__(mcl, name, bases, cdict)


if __name__ == '__main__':

    from meta_2_3 import with_metaclass


    class Typed(with_metaclass(TypeProtected)):
        pass

    class MyClass(Typed):
        """Test class."""
        attr1 = TypDescriptor(int)
        attr2 = TypDescriptor(float, 5.5)


    def main():
        """Test it.
        """
        my_inst = MyClass()
        print(my_inst.attr1)
        print(my_inst.attr2)
        print(dir(my_inst))
        print(my_inst.__slots__)
        my_inst.attr1 = 100
        print(my_inst.attr1)
        # this will fail
        try:
            my_inst.unknown = 100
        except AttributeError:
            print('cannot do this')

    main()
