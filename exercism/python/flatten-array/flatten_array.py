from collections import Iterable


def is_container_type(o):
    return isinstance(o, Iterable) and not isinstance(o, str)


def flatten(arr):
    out = []
    for a in arr:
        if is_container_type(a):
            out.extend(flatten(a))
        elif a is not None:
            out.append(a)
    return out
