import time

def timeit(func):
    def new_fonc(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("%s seconds" % (end - start))
        return result
    return new_fonc
