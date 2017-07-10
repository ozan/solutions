def flatten(arr):
    out = []
    for a in arr:
        if a is None:
            continue
        if hasattr(a, '__iter__'):
            out.extend(flatten(a))
        else:
            out.append(a)
    return out
