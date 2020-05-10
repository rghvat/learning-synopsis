# file: submeta.py

from meta_2_3 import with_metaclass

class BaseMetaClass(type):
    pass

class SubMetaClass(BaseMetaClass):
    pass

class BaseClass1(with_metaclass(BaseMetaClass)):
    pass

class BaseClass2(with_metaclass(SubMetaClass)):
    pass

class WorkingClass(BaseClass1, BaseClass2):
    pass