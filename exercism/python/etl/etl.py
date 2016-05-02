

def transform(given):
    return {v.lower(): k for k in given for v in given[k]}
