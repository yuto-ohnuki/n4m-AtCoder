from collections import deque

def main():
    k = int(input())
    que = deque([i for i in range(10)])
    ans = [i for i in range(1, 10)]
    for _ in range(10):
        nx = []
        while que:
            x = que.pop()
            for i in range(10):
                if i>int(str(x)[0]):
                    t = int(str(i)+str(x))
                    nx.append(t)
        nx.sort()
        ans += nx
        que = deque(nx)
    ans.sort()
    print(ans[k-1])

if __name__ == '__main__':
    main()