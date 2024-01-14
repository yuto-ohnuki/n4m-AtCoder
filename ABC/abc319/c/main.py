n,m = map(int, input().split())
l = list(map(int, input().split()))

def func(w):
    tmp = 0
    cnt = 1
    i = 0
    while i<n:
        if w<tmp+l[i]:
            cnt += 1
            tmp = 0

        if tmp+l[i]<=w:
            tmp += l[i] + 1
        
        i += 1
    
    if cnt <= m:
        return True
    else:
        return False

ng = max(l)-1
ok = 10**20

while 1<ok-ng:
    mid = (ok+ng)//2
    if func(mid):
        ok = mid
    else:
        ng = mid
print(ok)