# coding: utf-8


"""Example for descriptor that checks conditions on attributes.
"""
from __future__ import print_function

from weakref import WeakKeyDictionary


class Checked(object):
    """Descriptor that checks with a user-supplied check function
    if an attribute is valid.
    """

    def __init__(self, checker=None, default=None):
        self._values = WeakKeyDictionary()
        if checker:
            # checker must be a callable
            checker(default)
        self.checker = checker
        self.default = default

    def __get__(self, instance, owner):
        return self._values.get(instance, self.default)

    def __set__(self, instance, value):
        if self.checker:
            self.checker(value)
        self._values[instance] = value


if __name__ == '__main__':

    def is_int(value):
        """Check if value is an integer.
        """
        if not isinstance(value, int):
            raise ValueError('Int required {} found'.format(type(value)))

    class Restricted(object):
        """Use checked attributes.
        """
        attr1 = Checked(checker=is_int, default=10)
        attr2 = Checked(default=12.5)
        # Setting the default to float, `is_int` raises a `ValueError`.
        try:
            attr3 = Checked(checker=is_int, default=12.5)
        except ValueError:
            print('Cannot set default to float, must be int.')
            attr3 = Checked(checker=is_int, default=12)

    restricted = Restricted()
    print('attr1', restricted.attr1)
    restricted.attr1 = 100
    print('attr1', restricted.attr1)
    try:
        restricted.attr1 = 200.12
    except ValueError:
        print('Cannot set attr1 to float, must be int.')
        restricted.attr1 = 200
    print(restricted.attr1, restricted.attr2, restricted.attr3)
