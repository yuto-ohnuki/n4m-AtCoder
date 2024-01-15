def comb(f1,f2):
    return lambda x:f1(f2(x))

def is_unique(cols, sols):
    REV = lambda ls:list(reversed(ls))
    USD = lambda ls:[len(ls)-x-1 for x in ls]
    T90 = lambda ls:[(n-1)-ls.index(x) for x in range(len(ls))]
    T180 = comb(USD, REV)
    T270 = comb(T90, T180)
    D1 = comb(T90, REV)
    D2 = comb(T90, USD)
    flg = True
    for op in (REV, USD, T90, T180, T270, D1, D2):
        if tuple(op(cols)) not in sols:
            continue
        else:
            flg = False
            break
    return flg
    
def check(ls, nxt):
    flg = True
    for col, row in enumerate(ls):
        if abs(nxt-row)!=col+1:
            continue
        else:
            flg = False
            break
    return flg

def dfs(cols, rows, sols):
    if rows:
        for i in rows:
            if check(cols, i):
                dfs((i,)+cols, rows-{i}, sols)
    elif is_unique(cols, sols):
        sols.add(cols)

def solve(n):
    sols = set()
    dfs(tuple(), frozenset(range(n)), sols)
    return sols

def output(sol):
    ret = [['.']*n for _ in range(n)]
    for x,y in enumerate(sol):
        ret[y][x] = 'Q'
    for r in ret:
        print(*r)
    print('\n')

if __name__ == '__main__':
    n = int(input())
    sols = solve(n)
    print('{}-queen Solution :'.format(n),len(sols))
    for e, sol in enumerate(sols):
        print('Solution:{}'.format(e+1))
        output(sol)