import time
import datetime

def log(f):
    def inner(*args, **kwargs):
        start = time.time()
        print(f'start {f.__name__} {datetime.datetime.fromtimestamp(start)}')
        f(*args, **kwargs)
        print(f'total execution {f.__name__} {time.time() - start} s')

    return inner
