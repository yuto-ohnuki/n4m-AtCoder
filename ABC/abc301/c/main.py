from collections import defaultdict
from string import ascii_lowercase
def main():
    s = input()
    t = input()

    dic_s = defaultdict(int)
    dic_t = defaultdict(int)

    for c in s:
        dic_s[c] += 1
    for c in t:
        dic_t[c] += 1
    
    at_s, at_t = dic_s['@'], dic_t['@']
    flg = True

    for c in ascii_lowercase:
        if c in 'atcoder':
            if dic_s[c] == dic_t[c]:
                continue
            else:
                if dic_s[c] > dic_t[c]:
                    at_t -= (dic_s[c] - dic_t[c])
                else:
                    at_s -= (dic_t[c] - dic_s[c])
                
                if at_s<0 or at_t<0:
                    flg = False
                    break
        else:
            if dic_s[c] != dic_t[c]:
                flg = False
                break
    
    print("Yes" if flg else "No")

if __name__ == '__main__':
    main()