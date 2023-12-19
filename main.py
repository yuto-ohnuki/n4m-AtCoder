from collections import defaultdict

def zero_padding(x, digit):
    if isinstance(x, int):
        x = str(x)
    elif isinstance(x, str):
        pass
    else:
        raise Exception('Unexpected data type: {}'.format(x))
    return x.zfill(digit)

def main():
    n = int(input())
    s = input()
    ans = []
    for i in range(1000):
        tmp = zero_padding(i, 3)
        idx = 0

        for j in range(len(s)):
            if tmp[idx] == s[j]:
                idx += 1
            if idx >= len(tmp):
                ans.append(tmp)
                break

    print(len(ans))

if __name__ == '__main__':
    main()
