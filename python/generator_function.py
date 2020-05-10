'''
Generator Function Example

Usage
    1. consume data as it gets ready
    2. when Generator exhaust it sends StopIteration signal
    3. generator has close() signal to shutdown the generator, it is used when a generator is no longer used or deleted.
        for partially used generator close signal
    4. close is signaled by GeneratorExit exception occuring on yield statement
'''
import sys

def countdown(num):
    '''
    '''
    print('Function Name "{}" Counting down from {}'.format(countdown.__name__, num))
    while num>0:
        yield num
        num -= 1

if __name__ == '__main__':

    for i in countdown(10):
        print(i)

    c = countdown(10)
    while True:
        try:
            print(next(c))
            # 
            # 
        except StopIteration as e:
            print(e)
            break
    print('helo')