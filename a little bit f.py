
#A Little Bit Frightening


def find(parent, i):
    if (parent[i] == i):
        return i

    return find(parent, parent[i])


def Union(parent, x, y):
    xset = find(parent, x)
    yset = find(parent, y)
    parent[xset] = min(xset, yset)
    parent[yset] = min(xset, yset)
    num_of_groups[min(xset, yset)] += num_of_groups[max(xset, yset)]


T=int(input())
for l in range(T):
    N, L, Q = list(map(int, input().strip().split()))
    answers=[0 for p in range(Q)]
    alledges_queries=[]
    for p in range(L):

        v1, v2, val = list(map(int, input().strip().split()))
        alledges_queries.append([2*val,v1,v2])


    for x in range(Q):
        i, s = list(map(int, input().strip().split()))
        alledges_queries.append([2*s+1,i,x])

    alledges_queries.sort()

    parent = [t for t in range(N+1)]
    num_of_groups = [1 for w in range(N+1)]

    for e in alledges_queries:
        if e[0]%2==0:
            k1 = e[1]
            k2 = e[2]
            if (find(parent,k1)!=find(parent,k2)):
                Union(parent,k1,k2)

        else:

            answers[e[2]] = num_of_groups[find(parent, e[1])]

    for r in answers:
        print(r)