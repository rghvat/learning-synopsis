# file: autometa_python2.py

"""Example usage of a metaclass.

We change the metaclass of classes that inherit from `object`.
"""

from __future__ import print_function

import __builtin__


class DebugMeta(type):
    """Metaclass to be used for debugging.

    """
    names = []
    counter = -1  # Do not count definition of new_object`.

    def __init__(cls, name, bases, cdict):
        """Store all class names and count how many classes are defined.
        """
        if DebugMeta.counter >= 0:
            DebugMeta.names.append('%s.%s' % (cls.__module__, name))
            super(DebugMeta, cls).__init__(name, bases, cdict)
        DebugMeta.counter += 1

    def report(cls):
        print('Defined %d classes.' % DebugMeta.counter)
        print(DebugMeta.names)


class new_object(object):
    """Replacement for the built-in `object`.
    """
    __metaclass__ = DebugMeta


def set_new_meta():
    """We actually change a built-in. This is a very strong measure.
    """
    __builtin__.object = new_object





