def main():
    ha,wa = map(int, input().split())
    ga = [list(input()) for _ in range(ha)]

    hb,wb = map(int, input().split())
    gb = [list(input()) for _ in range(hb)]

    hx,wx = map(int, input().split())
    gx = [list(input()) for _ in range(hx)]


    mat = ['.'*10 for _ in range(10)]
    print(mat)

    for ia in range(10):
        for ja in range(10):
            idx_a = (ia, ja)
            

            for ib in range(10):
                for jb in range(10):
                    idx_b = (ib, jb)


                    
            
            

if __name__ == '__main__':
    main()
