from weakkeydict_storage import DescriptorWeakKeyDictStorage


class StoreInstance(object):
    """All instances have own `attr`.
    """
    attr1 = DescriptorWeakKeyDictStorage(10)
    attr2 = DescriptorWeakKeyDictStorage(-5)

    def __hash__(self):
        raise NotImplementedError
    #def __eq__(self, other):
    #    raise False

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