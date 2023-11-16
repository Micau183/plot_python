def fact(n):
    if n ==1 or n ==0:
        return 1
    else:
        return n*fact(n-1)


def remonte_parent(cycle, sommet):
    cycle.append(sommet)
    if sommet.parent is None:
        return cycle
    else:
        return remonte_parent(cycle, sommet.parent)


def dfs(sommet):
    sommet.visited = True
    pile = []
    cycles = []
    cycle = []
    pile.append(sommet)
    while pile != []:
        s = pile.pop()
        for voisin in s.voisins:
            if voisin.visited:
                return remonte_parent([], s)

            else:
                voisin.visited = True
                pile.append(voisin)
