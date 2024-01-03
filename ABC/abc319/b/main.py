def main():
    n = int(input())
    ans = []
    for i in range(n+1):
        s = float('inf')
        for j in range(1, 10):
            if n%j == 0:
                tmp = n//j
                if i%tmp == 0:
                    s = min(s, j)
        if s != float('inf'):
            ans.append(str(s))
        else:
            ans.append('-')
    print(''.join(ans))

if __name__ == '__main__':
    main()
