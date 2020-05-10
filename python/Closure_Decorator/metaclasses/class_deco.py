# file: class_deco.py

def noclassattr_deco(cls):
    """Class decorator to allow only callable attributes.
    """
    allowed = set(['__module__', '__metaclass__', '__doc__', '__qualname__',
                   '__weakref__', '__dict__'])
    for key, value in cls.__dict__.items():
        if (key not in allowed) and (not callable(value)):
            msg = 'Found non-callable class attribute "%s". ' % key
            msg += 'Only methods are allowed.'
            raise Exception(msg)
    return cls


if __name__ == '__main__':

    @noclassattr_deco
    class AttributeLess(object):
        """Only methods work.
        """
        def meth(self):
            """This is allowed'
            """
            print('Hello from AttributeLess.')

    attributeless = AttributeLess()
    attributeless.meth()

    @noclassattr_deco
    class WithAttribute(object):
        """Has non-callable class attribute.
        Will raise an exception.
        """
        a = 10
        def meth(self):
            """This is allowed'
            """
            print('Hello from WithAttribute')