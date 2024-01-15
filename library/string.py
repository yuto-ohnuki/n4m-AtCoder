""" 数値 (str) を右寄せゼロ埋め """
def zero_padding(x, digit):
    if isinstance(x, int):
        x = str(x)
    elif isinstance(x, str):
        pass
    else:
        raise Exception('Unexpected data type: {}'.format(x))
    return x.zfill(digit)
