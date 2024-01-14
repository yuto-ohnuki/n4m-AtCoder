def main():
    s = input()
    ans = -1
    for i in range(len(s)+1):
        for j in range(i+1, len(s)+1):
            tmp = s[i:j]
            if tmp == tmp[::-1]:
                ans = max(ans, len(tmp))
    print(ans)

if __name__ == '__main__':
    main()
