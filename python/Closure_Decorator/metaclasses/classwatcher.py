# file: classwatcher.py

"""Find all defined classes.

Needs Python 3.
"""

import builtins
from collections import Counter


class MultipleInstancesError(Exception):
    """Allow only one instance.
    """
    pass


class ClassWatcher(object):
    """After instantiation of this class, all newly defined classes will
       be counted.

    Only one instance of this class is allowed.
    """

    def __new__(cls, only_packages=frozenset(), ignore_packages=frozenset()):
        """
        only_packages: positive list of package names
                       Only these packages will be used.
        ignore_packages: negative list of package names
                         These packages will not be considered.

        The names in both sets are checked with `.startwith()'.
        This allows to filter for  `package` or `package.subpackage` and
        so on.
        For example, you can include `package` with `only_packages` and
        and then exclude `package.subpackage` with ignore_packages`.
        """
        if hasattr(cls, '_instance_exists'):
            msg = 'Only one instance of ClassWatcher allowed.'
            raise MultipleInstancesError(msg)
        cls._instance_exists = True
        cls.defined_classes = Counter()
        cls.activate(only_packages, ignore_packages)
        return super().__new__(cls)

    @staticmethod
    def __build_class__(func, name, *bases, metaclass=type, **kwds):
        """Replacement for the the built-in `__build_class__`.

        Use on your own risk.
        """
        name = '{}.{}'.format(func.__module__, func.__qualname__)

        if not ClassWatcher.only_packages:
            add_name = True
        else:
            add_name = False
            for p_name in ClassWatcher.only_packages:
                if name.startswith(p_name):
                    add_name = True
        for p_name in ClassWatcher.ignore_packages:
            if name.startswith(p_name):
                add_name = False
        if add_name:
            ClassWatcher.defined_classes[name] += 1
        cls = ClassWatcher.orig__build_class__(func, name, *bases,
                                               metaclass=metaclass, **kwds)
        return cls

    @classmethod
    def activate(cls, only_packages=frozenset(), ignore_packages=frozenset()):
        """Replace the built-in `__build_class__` with a customer version.
        """
        cls.orig__build_class__ = builtins.__build_class__
        builtins.__build_class__ = cls.__build_class__
        cls.only_packages = frozenset(only_packages)
        cls.ignore_packages = frozenset(ignore_packages)

    @classmethod
    def deactivate(cls):
        """Set built-in `__build_class__` back to real built-in.
        """
        builtins.__build_class__ = cls.orig__build_class__

    def report(self, limit=20):
        """Show results.
        """
        print('total defined classes:', sum(self.defined_classes.values()))
        print('total unique classes: ', len(self.defined_classes))
        all_names = self.defined_classes.most_common()
        width = max(len(name[0]) for name in all_names[:limit])
        count_width = 10
        print('{:{width}}{:>{count_width}}'.format('Name', 'Count',
            width=width, count_width=count_width))
        print('#' * (width + count_width))
        for counter, (cls_name, count) in enumerate(all_names, 1):
            print('{:{width}s}{:{count_width}d}'.format(cls_name, count,
                width=width, count_width=count_width))
            if counter >= limit:
                print('...')
                print('Skipped', len(all_names) - counter, 'additional lines.')
                break
