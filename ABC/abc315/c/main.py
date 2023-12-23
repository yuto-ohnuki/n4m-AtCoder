from collections import defaultdict
def main():
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]

    dic = defaultdict(list)
    for i in range(n):
        f,s = lst[i]
        dic[f].append(s)
    
    nx_dic = {k:sorted(v, reverse=True) for k,v in dic.items()}
    mx_vals = sorted([max(v) for v in dic.values()], reverse=True)

    tmp = -1
    for k,v in nx_dic.items():
        if len(v)>=2:
            tmp = max(tmp, v[0]+v[1]//2)
    
    if len(mx_vals) >= 2:
        tmp = max(tmp, mx_vals[0] + mx_vals[1])
    
    print(tmp)

if __name__ == '__main__':
    main()
