# file: meta_2_3.py

"""
The code is a bit hard to understand. The basic idea is exploiting the idea
that metaclasses can customize class creation and are picked by by the parent
class. This particular implementation uses a metaclass to remove its own parent
from the inheritance tree on subclassing. The end result is that the function
creates a dummy class with a dummy metaclass. Once subclassed the dummy
classes metaclass is used which has a constructor that basically instances a
new class from the original parent and the actually intended metaclass.
That way the dummy class and dummy metaclass never show up.

From:
 http://lucumr.pocoo.org/2013/5/21/porting-to-python-3-redux/#metaclass-syntax-changes

Used in:

* Jinja2
* SQLAlchemy
* future (python-future.org)

"""

from __future__ import print_function
import platform


# from jinja2/_compat.py
def with_metaclass(meta, *bases):
    # This requires a bit of explanation: the basic idea is to make a
    # dummy metaclass for one level of class instanciation that replaces
    # itself with the actual metaclass.  Because of internal type checks
    # we also need to make sure that we downgrade the custom metaclass
    # for one level to something closer to type (that's why __call__ and
    # __init__ comes back from type etc.).
    #
    # This has the advantage over six.with_metaclass in that it does not
    # introduce dummy classes into the final MRO.
    class metaclass(meta):
        __call__ = type.__call__
        __init__ = type.__init__

        def __new__(cls, name, this_bases, d):
            if this_bases is None:
                return type.__new__(cls, name, (), d)
            return meta(name, bases, d)

    return metaclass('temporary_class', None, {})


if __name__ == '__main__':

    class BaseClass(object):
        pass


    class MetaClass(type):
        """Metaclass for Python 2 and 3.
        """
        def __init__(cls, name, bases, cdict):
            print('It works with {impl} version {ver}.'.format(
                impl=platform.python_implementation(),
                ver=platform.python_version()))
            super(MetaClass, cls).__init__(name, bases, cdict)


    class Class(with_metaclass(MetaClass, BaseClass)):
        # BaseClass is optional.
        pass
