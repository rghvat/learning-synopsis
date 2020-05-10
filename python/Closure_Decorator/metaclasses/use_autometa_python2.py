# file: use_autometa_python2.py

from autometa_python2 import set_new_meta

set_new_meta()

class SomeClass1(object):
    """Test class.
    """
    pass


class SomeClass2(object):
    """Test class.
    """
    def __init__(self, arg1):
        self.arg1 = arg1

    def compute(self, arg2):
        return self.arg1 + arg2


class SomeClass3():
    """Test class. Does NOT inherit from object.
    """
    pass


if __name__ == '__main__':

    def test():
        """Make an instance and write the report.
        """
        inst = SomeClass2(10)
        assert inst.compute(10) == 20
        object.report()

    test()
