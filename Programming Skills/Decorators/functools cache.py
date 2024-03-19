import functools

# When calling the same function repeatedly with the same arguments,
# using cache will save the already calculated values and decrease processing
@functools.cache
def fibonacci(n):
    """ Calculating fibonacci value """
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(40))
