from collections import deque
def main():
    n = int(input())
    s = input()

    que = deque([[]])
    for c in s:
        if c!='(' and c!=')':
            que[-1].append(c)
        elif c=='(':
            que.append([])
            que[-1].append('(')
        elif c==')':
            if len(que)!=1:
                que.pop()
            else:
                que[-1].append(')')
        else:
            pass
    
    ans = ''
    while que:
        x = que.popleft()
        ans += ''.join(x)
    print(ans)

if __name__ == '__main__':
    main()
