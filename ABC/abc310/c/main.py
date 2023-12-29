def main():
    n = int(input())
    dic = {}
    used = set([])
    cnt = 0
    for _ in range(n):
        s = input()
        if s in used:
            continue

        else:
            cnt += 1
            used.add(s)
            used.add(s[::-1])
    print(cnt)

if __name__ == '__main__':
    main()
