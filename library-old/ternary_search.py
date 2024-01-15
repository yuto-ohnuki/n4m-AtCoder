""" 三分探索を行う関数 """
def ternary_search(high, low, epsilon=1e-8):
    
    """ 極地を求める凸関数を定義 """
    def f(x):
        return 0
    
    while high - low > epsilon:
        mid_left = high*(1/3) + low*(2/3)
        mid_right = high*(2/3) + low*(1/3)
        if f(mid_left) >= f(mid_right):
            low = mid_left
        else:
            high = mid_right
    
    return high