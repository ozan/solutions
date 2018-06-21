

def unique(xs):
    return list(set(xs))

def product(xs, ys):
    return [x + y for x in xs for y in ys]

def wrap(xs):
    return ['(' + x + ')' for x in xs]

def concat(a, b):
    return a + b

def memoize_method(f):
    cache = {}
    def inner(context, arg):
        try:
            return cache[arg]
        except KeyError:
            result = f(context, arg)
            cache[arg] = result
            return result
    return inner
            

class Solution(object):

    @memoize_method
    def generateParenthesis(self, n):
        if n == 0:
            return []
        if n == 1:
            return ['()']
        xs = [self.generateParenthesis(m) for m in range(1, n)]
        ys = reversed(xs)
        prod = reduce(concat, [product(x, y) for x, y in zip(xs, ys)], [])
        return unique(prod + wrap(xs[-1]))
    
