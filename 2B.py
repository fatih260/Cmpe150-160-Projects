# Merging powers of robots with find and union algorithms

import math
n,m = list(map(int, input().strip().split()))
powers = list(map(int, input().strip().split()))
powers.insert(0,0)
parent = [k for k in range(0,n+2)]

def bitwaseOr(p1, p2):
    if p1 == p2:
        return p1
    s = math.floor(math.log2(p1))
    if 2**s>p2:
        if p1 - 2 ** s >= p2:
            return 2**s + bitwaseOr(p1-2**s,p2)
        else:
            return 2**s + bitwaseOr(p2,p1-2**s)
    else:
        return 2 ** s + bitwaseOr(p1-2**s,p2-2**s)

def find(parent, i):
    if (parent[i] == i):
        return i

    return find(parent, parent[i])


def Union(parent, x, y):
    xset = find(parent, x)
    yset = find(parent, y)
    if xset < yset:
        parent[yset] = xset
    elif yset < xset:
        parent[xset] = yset

res = []
for i in range(m):
    query = list(map(int, input().strip().split()))
    r1 = query[0]
    r2 = query[1]
    if find(parent, r1) != find(parent, r2):
        p1 = powers[find(parent, r1)]
        p2 = powers[find(parent, r2)]
        Union(parent,r1,r2)

        if p1 > p2:
            y = bitwaseOr(p1,p2)
            res.append(y)
            powers[find(parent, r1)] = y


        elif p2 > p1:
            y = bitwaseOr(p2,p1)
            res.append(y)
            powers[find(parent, r1)] = y


        if p1 == p2:
            res.append(p1)
            powers[find(parent, r1)] = p1


    else:
        res.append(-1)

for e in res:
    print(e)
