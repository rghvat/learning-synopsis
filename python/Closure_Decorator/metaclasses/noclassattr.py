#file: noclassattr.py

"""Preventing non-callable class attributes with a metaclass.
"""

from __future__ import print_function

class NoClassAttributes(type):
    """No non-callable class attributes allowed
    """
    def __init__(cls, name, bases, cdict):
        allowed = set(['__module__', '__metaclass__', '__doc__',
                       '__qualname__'])
        for key, value in cdict.items():
            if (key not in allowed) and (not callable(value)):
                msg = 'Found non-callable class attribute "%s". ' % key
                msg += 'Only methods are allowed.'
                raise Exception(msg)
        super(NoClassAttributes, cls).__init__(name, bases, cdict)


if __name__ == '__main__':

    from meta_2_3 import with_metaclass

    class AttributeChecker(with_metaclass(NoClassAttributes)):
        """Base class for meta.
        """
        pass

    class AttributeLess(AttributeChecker):
        """Only methods work.
        """
        def meth(self):
            """This is allowed'
            """
            print('Hello from AttributeLess.')

    attributeless = AttributeLess()
    attributeless.meth()


    class WithAttribute(AttributeChecker):
        """Has non-callable class attribute.
        Will raise an exception.
        """
        a = 10
        def meth(self):
            """This is allowed'
            """
            print('Hello from WithAttribute')

