def main():
    n,d,p = map(int, input().split())
    f = sorted(list(map(int, input().split())), reverse=True)
    i = 0
    ans = 0
    while True:
        cand = f[i*d:(i+1)*d]
        if sum(cand) > p:
            ans += p
            i += 1
        else:
            ans += sum(f[i*d:])
            break
    print(ans)
    
if __name__ == '__main__':
    main()
