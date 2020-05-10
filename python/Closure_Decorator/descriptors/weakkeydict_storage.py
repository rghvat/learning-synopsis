# coding: utf-8

"""A descriptor works only in a class.

We can store a different value for each instance in a dictionary
in the descriptor.
"""

from __future__ import print_function

from weakref import WeakKeyDictionary


class DescriptorWeakKeyDictStorage(object):
    """Descriptor that stores attribute data in instances.
    """

    def __init__(self, default=None):
        self._hidden = WeakKeyDictionary()
        self.default = default

    def __get__(self, instance, owner):
        return self._hidden.get(instance, self.default)

    def __set__(self, instance, value):
       self._hidden[instance] = value


if __name__ == '__main__':
    class StoreInstance(object):
        """All instances have own `attr`.
        """
        attr1 = DescriptorWeakKeyDictStorage(10)
        attr2 = DescriptorWeakKeyDictStorage(-5)


    store1 = StoreInstance()
    store2 = StoreInstance()
    print('store1', store1.attr1)
    print('store2', store2.attr1)
    print('Setting store1 only.')
    store1.attr1 = 100
    store1.attr2 = -123
    store2.attr1 = 98765
    print('store1 attr1', store1.attr1)
    print('store1 attr2', store1.attr2)
    print('store2', store2.attr1)
    print('_hidden:', list(StoreInstance.__dict__['attr1']._hidden.items()))
    print('_hidden:', list(StoreInstance.__dict__['attr2']._hidden.items()))
    del store1
    print('Deleted store1')
    print('_hidden:', list(StoreInstance.__dict__['attr1']._hidden.items()))

