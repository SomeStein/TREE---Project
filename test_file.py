import time

start = time.time()


def combinations(n, k):
    if k == 1:
        l = list(range(n))
        return [(x,) for x in l]
    l = combinations(n, k-1)
    return [(x, *t) for x in range(n) for t in l]


c = combinations(10, 8)

print("took: ", time.time()-start)
