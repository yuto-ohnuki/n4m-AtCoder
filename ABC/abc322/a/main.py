def main():
    n = int(input())
    s = input()
    ans = -1
    for i in range(3, n+1):
        if s[i-3:i] == "ABC":
            ans = i-2
            break
    print(ans)
if __name__ == '__main__':
    main()
