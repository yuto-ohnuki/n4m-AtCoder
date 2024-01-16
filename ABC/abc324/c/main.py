
def func(x,y):
    
    # x: longer than y
    if len(x) < len(y):
        x,y = y,x
    
    rx = x[::-1]
    ry = y[::-1]

    if len(x) == len(y):
        dif = 0
        for i in range(len(x)):
            if x[i]!=y[i]:
                dif += 1
        return dif <= 1
    
    else:
        if len(x) - len(y) > 1:
            return False
        
        else:
            pass
            # ここを修正する

def main():
    n,t = input().split()
    s = [input() for _ in range(int(n))]
    ans = []
    for i in range(int(n)):
        if func(t, s[i]):
            ans.append(i+1)

    print(len(ans))
    print(*ans)

if __name__ == '__main__':
    main()