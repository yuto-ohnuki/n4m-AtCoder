import math
from decimal import Decimal
def main():
    a,b = map(int, input().split())
    print(math.ceil(Decimal(a)/Decimal(b)))

if __name__ == '__main__':
    main()
