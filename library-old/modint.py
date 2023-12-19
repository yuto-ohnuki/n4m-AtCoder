"""適用するMODの定義(任意)"""
MOD = 3

class ModInt:
    def __init__(self, x):
        self.x = x%MOD
    
    """str関数を適用した場合に、intと同一の文字列を返す"""
    def __str__(self):
        return str(self.x)
    
    """print関数を適用した場合に、intと同一の文字列を返す"""
    __repr__ = __str__
    
    """和"""
    def __add__(self, other):
        """otherがModInt型のインスタンスならTrue"""
        if isinstance(other, ModInt):
            ret = ModInt(self.x + other.x)
        else:
            ret = ModInt(self.x + other)
        return ret
    
    """差"""
    def __sub__(self, other):
        if isinstance(other, ModInt):
            ret = ModInt(self.x - other.x)
        else:
            ret = ModInt(self.x - other)
        return ret
    
    """積"""
    def __mul__(self, other):
        if isinstance(other, ModInt):
            ret = ModInt(self.x * other.x)
        else:
            ret = ModInt(self.x * other)
        return ret
    
    """商"""
    """mod Mにおける逆元を求めて、逆元との積で商を実装"""
    def __truediv__(self, other):
        if isinstance(other, ModInt):
            ret = ModInt(other.x * pow(self.x, MOD-2, MOD))
        else:
            ret = ModInt(other * pow(self.x, MOD-2, MOD))
        return ret
    
    """乗算"""
    def __pow__(self, other):
        if isinstance(other, ModInt):
            ret = ModInt(pow(self.x, other.x, MOD))
        else:
            ret = ModInt(pow(self.x, other, MOD))
        return ret
    
    
    """接頭辞がrのメソッドを定義することにより、int,ModIntの順序での演算を可能とする"""
    __radd__ = __add__
    
    def __rsub__(self, other):
        if isinstance(other, ModInt):
            ret = ModInt(other.x - self.x)
        else:
            ret = ModInt(other - self.x)
        return ret
    
    __rmul__ = __mul__
    
    def __rtruediv__(self, other):
        if isinstance(other, ModInt):
            ret = ModInt(other.x * pow(self.x, MOD-2, MOD))
        else:
            ret = ModInt(other * pow(self.x, MOD-2, MOD))
        return ret
    
    def __rpow__(self, other):
        if isinstance(other, ModInt):
            ret = ModInt(pow(other.x, self.x, MOD))
        else:
            ret = ModInt(pow(other, self.x, MOD))
        return ret
    

#Example of Uses
"""
#除算 -> x/y mod Mを計算
x,y = map(ModInt, (map(int,input().split()))
print(x / y)

#(int)との演算
#乗算　-> (x*y)**z mod Mを計算
x = ModInt(int(input()))
y,z = map(int,input().split())
print((x+y)**z)

#sum関数
#Sum(i**z) mod M
n,z = map(int,input().split())
print(sum(ModInt(i)**z for i in range(1, n+1)))"""