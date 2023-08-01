""" 約数の列挙 """
def divisor(x):
    ret = []
    for i in range(1, int(x**0.5)+1):
        if x%i==0:
            ret.append(i)
            if not i**2 == x:
                ret.append(x//i)

    # ret.sort()
    return ret