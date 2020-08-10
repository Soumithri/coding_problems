
def fib(n):
    cache = {}
    return _fib(n, cache)


def _fib(n, cache):
    if n < 0:
        raise Exception('negative number')
    elif n in [0, 1]:
        return n
    if n in cache:
        return cache[n]
    cache[n] = _fib(n-1, cache) + _fib(n-2, cache)
    return cache[n]
