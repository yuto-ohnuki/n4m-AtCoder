def main():
    n = int(input())
    s = input()
    q = int(input())

    ans = list(s)
    que = [input().split() for _ in range(q)]
    line = -1

    for i, (t,x,c) in enumerate(que):
        if t == '2' or t == '3':
            line = i
    
    for i, (t,x,c) in enumerate(que):
        if t == '1':
            ans[int(x)-1] = c
        elif t == '2' and i == line:
            ans = list(''.join(ans).lower())
        elif t == '3' and i == line:
            ans = list(''.join(ans).upper())
        
    print(''.join(ans))


if __name__ == '__main__':
    main()
