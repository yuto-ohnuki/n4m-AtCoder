""" Segment Tree """
# 結合則が成立し、単位元が存在するモノイドが存在することが条件
# 決まった性質を満たす操作、演算に対する区間クエリをO(logN)で求めるデータ構造
# データ構築はO(logN)

class Seg_tree:
    def __init__(self, n, operator, identity):
        """
            n : データ配列のサイズ
            operator : 演算子(モノイド)
            identiry : 演算子に対する単位元
                        ・ min -> identity : 10**10
                        ・ max -> identity : -1
                        ・ xor -> identity : 0
                        ・ or -> identity : 0                        
        """
        nb = format(n, 'b')
        bc = sum([int(digit) for digit in nb])
        if bc==1:
            self.num_end_leaves = 2**(len(nb)-1)
        else:
            self.num_end_leaves = 2**(len(nb))
        
        self.array = [identity for i in range(self.num_end_leaves*2)]   # 配列を単位元で初期化
        self.identity = identity
        self.operator = operator
    
    """ 値の更新を行う関数 """
    def update(self, x, val):
        """
            x : 代入するindex
            val : 代入するvalue
        """
        actual_x = x + self.num_end_leaves
        self.array[actual_x] = val    # 値の更新
        while actual_x > 0:
            actual_x = actual_x // 2
            self.array[actual_x] = self.operator(self.array[actual_x*2], self.array[actual_x*2+1])
    
    """ 値の取得を行う関数 """
    def get(self, q_left, q_right, arr_ind=1, leaf_left=0, depth=0):
        """
            q_left : クエリ期間の左端
            q_right : クエリ期間の右端
            arr_ind : 木配列のindex
            leaf_left : 木配列のindexに対して、それを表す葉が被覆する範囲の左点
            depth : 木配列での深さ
        """
        
        width_of_floor = self.num_end_leaves // (2**depth)  #現在の葉のカバー幅
        leaf_right = leaf_left + width_of_floor - 1     # 左端とカバー幅から今の葉のカバー幅の右端を求める
        
        if leaf_left > q_right or leaf_right < q_left:  # クエリ領域と葉が関係ない場合単位元を返す 
            return self.identity
        elif leaf_left >= q_left and leaf_right <= q_right:     # クエリ領域に葉が被覆される場合には、葉の値を返す
            return self.array[arr_ind]
        else:   # それ以外の場合、子の値を参照して演算処理 -> 部分領域をマージ
            val_l = self.get(q_left, q_right, 2*arr_ind, leaf_left, depth+1)
            val_r = self.get(q_left, q_right, 2*arr_ind+1, leaf_left+width_of_floor//2 , depth+1)
            return self.operator(val_l,val_r)

# 動作確認 (RMQ : Range Minimum Query)
n = 5
A = [1,4,3,2,4]
seg_tree = Seg_tree(n=n, operator=min, identity=10**5)
for i,a in enumerate(A):
    seg_tree.update(i, a)
print('Array : ', *A)
print("Range 2:3 RMQ : ", seg_tree.get(2,3))
print("Range 0:2 RMQ : ", seg_tree.get(0,2))