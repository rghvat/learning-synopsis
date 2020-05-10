# file: base_conflict.py

from meta_2_3 import with_metaclass

class MetaClass1(type):
    pass

class MetaClass2(type):
    pass

class BaseClass1(with_metaclass(MetaClass1)):
    pass

class BaseClass2(with_metaclass(MetaClass2)):
    pass

class DoesNotWorkClass(BaseClass1, BaseClass2):
    pass