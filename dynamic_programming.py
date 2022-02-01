"""
Example on Dynamic Programming ...
"""
def fibb_slow(n):
    if n < 2:
        return n
    else:
        return fibb_slow(n - 1) + fibb_slow(n - 2)

fibbs = [0,1]
def fibb_fast(n):
    if n < 2:
        return fibbs[n]
    else:
        fibbs.append( fibbs[n-1] + fibbs[n-2] )
        return fibbs[-1]

for i in range(10):
    # print(fibb_slow(i), end=" ") # Did not finish on my machine
    print(fibb_fast(i), end=" ") # Instant
    # pass

# print(fibb_fast(10))