'''
Coroutine
    1. yield statement is on right side of assignment
    2. Data proccesser
    3. 
'''

def receiver():
    '''
    '''
    print('Ready to Receive')
    while True:
        n = (yield)
        print('Got {}'.format(n))

if __name__ == '__main__':
    r = receiver()
    next(r)
    r.send('Ragma')
    r.send('kin')

