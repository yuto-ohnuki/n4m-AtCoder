
"""Binary Indexed Tree (Fenwick Tree)"""
# 配列Aに対して、部分和と要素の更新クエリをO(logN)で行えるデータ構造
# 延長として、転倒数(i<jかつAi>Ajを満たす(i,j)の組の個数)を数えることが可能

class BIT:
    def __init__(self, n):
        """
            data : BIT木データ
            el : 元配列
        """
        self.n = n
        self.data = [0]*(n+1)
        self.el = [0]*(n+1)
    
    """A1 ~ Aiまでの累積和"""
    def Sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & (-i)   #LSB(Least Significant Bit)の獲得:i&(-i)
        return s
    
    """Ai += x"""
    def Add(self, i, x):
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i
    
    """Ai ~ Ajまでの累積和"""
    def Get(self, i, j=None):
        if j is None:
            return self.el[i]
        return self.Sum(j) - self.Sum(i)
    
    
""" RSQ(Range Sum Query) and RAQ(Range Add Query) - BITver"""
# BITデータ構造により配列Aに対して以下のクエリをO(logN)で行う
#   ・ Add　：　区間[l:r)に対してxを加算
#   ・ Sum　：　区間[l:r)の総和を求める
class Range_BIT:
    def __init__(self, n):
        self.n = n
        self.bit0 = [0]*(n+1)
        self.bit1 = [0]*(n+1)
    
    def _Add(self, k, x, is_bit0=True):
        if is_bit0 == True:
            data = self.bit0
        else:
            data = self.bit1
        while k <= self.n:
            data[k] += x
            k += k & -k
    
    def _Get(self, data, k):
        s = 0
        while k:
            s += data[k]
            k -= k&-k
        return s
    
    """ 配列の獲得 """
    def Array(self):
        array = [0]*(n+1)
        for i in range(self.n):
            array[i] = self.Get(i+1,i+2)
        return array[:-1]
    
    """ 区間[l:r)に対してxを加算 """
    def Add(self, l, r, x):
        self._Add(l, -x*(l-1), is_bit0=True)
        self._Add(r, x*(r-1), is_bit0=True)
        self._Add(l, x, is_bit0=False)
        self._Add(r, -x, is_bit0=False)
    
    """ 区間[l:r)の総和 """
    def Get(self, l, r):
        Pi = self._Get(self.bit1, r-1)*(r-1) - self._Get(self.bit1, l-1)*(l-1)
        Qi = self._Get(self.bit0, r-1) - self._Get(self.bit0, l-1)
        return Pi+Qi

    
"""転倒数のカウント"""
def invNumCount(lst):
    res = 0
    bit = BIT(max(lst))
    for i, p in enumerate(lst):
        bit.Add(p, 1)
        res += i+1 - bit.Sum(p)
    return res

#転倒数
lst = [3,10,1,8,5]
print('元配列', lst)
print('転倒数　：　{}個'.format(invNumCount(lst)))     #5個 : (3,1),(10,1),(10,8),(10,5),(8,5)

print('---------------------------')

# 動作確認
n = 6
A = [1,2,3,4,5,6]
bit = BIT(len(A))
for i, a in enumerate(A):
    bit.Add(i+1, a)
print('元配列', bit.el)
print('A1~A3の累積和', bit.Sum(3))
print('A1~A3の累積和', bit.Get(0, 3))
print('A3~A6の累積和', bit.Get(2, 6))

print('---------------------------')


# 動作確認
rbit = Range_BIT(n)
B = [1,2,3,4,5,6]
for i, b in enumerate(B):
    rbit.Add(i+1, i+2, b)
print('元配列', rbit.Array())
rbit.Add(2,4,10)                #　区間[2:4)に10を加算
print('配列  ', rbit.Array())