def main():
    n = int(input())
    a = list(map(int, input().split()))
    print("Yes" if len(list(set(a)))==1 else "No")

if __name__ == '__main__':
    main()
