

def make_change(target, parts):
    cache = [0]
    for i in range(1, target + 1):
        cache.append(1 + min(cache[i - c] for c in parts if c <= i))
    return cache[i]


print(make_change(40, (1,5,10,20,25,50)))
print(make_change(19159, (1,3,5,9,17)))
