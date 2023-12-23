def main():
    s = input()
    out = {'a', 'e', 'i', 'o', 'u'}

    ans = ''
    for c in s:
        if c not in out:
            ans += c
            
    print(ans)

if __name__ == '__main__':
    main()
