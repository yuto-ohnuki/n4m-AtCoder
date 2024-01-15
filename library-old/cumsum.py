"""累積和の計算"""

# 1次元
def f(lst):
    import numpy as np
    return np.cumsum([0] + lst)
l = [i for i in range(10)]
print('1次元')
print('\t', '元配列　：', l)
print('\t', '累積和　：', f(l).tolist())


# 2次元
""" 二次元累積配列を構築する関数 """
def make_array(h,w,a):
    da = [[0]*w for _ in range(h)]
    da[0][0] = a[0][0]
    for i in range(1, w):
        da[0][i] = da[0][i-1] + a[0][i]
    for i in range(1, h):
        cnt_w = 0
        for j in range(w):
            cnt_w += a[i][j]
            da[i][j] = da[i-1][j] + cnt_w
    return da

""" (p,q,x,y) : ４点：(p,q),(x,q),(p,y),(x,y)の長方形における２次元累積配列の和 """
def calc(p,q,x,y, da):
    if p>x  or q>y:
        return 0
    if p==0 and q==0:
        return da[x][y]
    if p==0:
        return da[x][y] - da[x][q-1]
    if q==0:
        return da[x][y] - da[p-1][y]
    return da[x][y] - da[x][q-1] - da[p-1][y] + da[p-1][q-1]

h,w = 3,4
c = [[4,6,2,5],
     [3,5,6,7],
     [2,5,5,6]]
da = make_array(h,w,c)
print('2次元')
print('\t', '元配列 : ')
for c_ in c:
    print('\t'*2, c_)
print('\t', '累積配列 : ')
for d in da:
    print('\t'*2, d)
print('\t', '(1,2)~(2,3)の累積和 : ', calc(1,2,2,3,da))
