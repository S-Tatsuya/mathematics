# Software Design ２０２３年５月号の数学特集の学習

- [Amazonリンク](https://www.amazon.co.jp/Software-Design-ソフトウェアデザイン-2023年5月号-雑誌-ebook/dp/B0C1J9BMWT/ref=sr_1_5?qid=1689412419&s=books&sr=1-5)
- 学習状況
    - [ ] 第1章 確率・統計
    - [ ] 第2章 微分・積分
    - [x] 第3章 線形代数
    - [ ] 第4章 集合・位相

## 第1章 確率・統計

## 第2章 微分・積分

## 第３章 線形代数

### 行列

- 行列のメリットは膨大なデータを扱う場合も同じルールで計算できる

- 行列の表現：
    - 2 x 2行列
$$A = \begin{pmatrix}
   1 & 1 \\
   2 & 4
\end{pmatrix}$$
    - 2 x 1行列
$$y = \begin{pmatrix}
    y_1 \\
    y_2
\end{pmatrix}$$
$$x = \begin{pmatrix}
    x_1 \\
    x_2
\end{pmatrix}$$
    - 足し算・引き算
$$\begin{pmatrix}
    a_{11} & a_{12} \\
    a_{21} & a_{22}
\end{pmatrix} \pm
\begin{pmatrix}
    b_{11} & b_{12} \\
    b_{21} & b_{22}
\end{pmatrix} =
\begin{pmatrix}
    a_{11} \pm b_{11}& a_{12} \pm b_{12} \\
    a_{21} \pm b_{21} & a_{22} \pm b_{22}
\end{pmatrix}$$
    - 定常倍
$$k\begin{pmatrix}
    a_{11} & a_{12} \\
    a_{21} & a_{22}
\end{pmatrix} =
\begin{pmatrix}
    ka_{11} & ka_{12} \\
    ka_{21} & ka_{22}
\end{pmatrix}$$
    - 行列の積: $A_{23} * B_{32} = C_{22}$
$$\begin{pmatrix}
    a_{11} & a_{12} & a_{13} \\
    a_{21} & a_{22} & a_{23}
\end{pmatrix}
\begin{pmatrix}
    b_{11} & b_{12} \\
    b_{21} & b_{22} \\
    b_{31} & b_{32}
\end{pmatrix} =
\begin{pmatrix}
    a_{11}b_{11} + a_{12}b_{21} + a_{13}b_{31} &
    a_{11}b_{12} + a_{12}b_{22} + a_{13}b_{32}\\
    a_{21}b_{11} + a_{22}b_{21} + a_{23}b_{31} &
    a_{21}b_{12} + a_{22}b_{22} + a_{23}b_{32}
\end{pmatrix}$$

- 結合法則、分配法則も成り立つ
    - ただし、積の計算ができないような行列同士の場合は計算自体ができない
        - 結合法則
$$(AB)C = A(BC)$$
        - 分配法則
$$A(kB + lC) = kAB + lAC$$

- 単位行列
    - 体格成分が全て `1` でそれ以外が全て `0` の正方行列
$$ l =
\begin{pmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1 \\
\end{pmatrix}$$
    - 記号 `I` を用いて表現される
    - 西方行列同士の掛け算では単位行列をかけても結果が変わらない
    - 通常の数字の `1` と同じ扱いになる。$A * 1 = A$ と同様

$$ AI = IA = A$$

- 逆行列
    - 任意の正方行列 $A$ に対して積を取ると $I$ になる正方行列 $A^{-1}$ のこと
    $$ AA^{-1} = A^{-1}A = 1$$
    - 通常の数字の $1/A$ と同じ扱いになる。 $ A * \cfrac{1}{A} = 1 $
    - 行列の計算には割り算は**ない**。逆行列が割り算の代わりに使われる
    - 任意の正方行列に対して**必ず逆行列が存在するわけではない**。

- 行列式
    - 任意の正方行列$A$に対して逆行列が存在するかを判定する式
    - `detA` の値が0でなければ、逆行列 $A^{-1}$ が存在する
    - 行列の大きさによって公式が少しかわるのかもしれない
    - 2 * 2の行列の公式を示す
        - 任意の正方行列 `A`
            $$A =
            \begin{pmatrix}
                a & b \\
                c & d
            \end{pmatrix}$$
        - 行列式
            $$ detA = ad - bc $$
        - 逆行列
            $$ A^{-1} = \cfrac{1}{detA}
            \begin{pmatrix}
                d & -b \\
                -c & a
            \end{pmatrix} =
            \cfrac{1}{ad - bc}
            \begin{pmatrix}
                d & -b \\
                -c & a
            \end{pmatrix}
            $$
    - 同じサイズの正方行列$A$、$B$に対して以下の関係が成り立つ
        $$ det(AB) = detA * detB $$
        $$ (AB)^{-1} = B^{-1}A^{-1} $$

#### 行列のPythonコード

- 行列はPythonではリストを使って表す

- 積の計算コード

    ```python
    def matmul(A, B):
        assert len(A[0]) == len(B)
        N, K, M = len(A), len(A[0]), len(B[0])
        C = [[0 for m in range(M)] for n in range(N)]
        for n in range(N):
            for m in range(M):
                C[n][m] = sum(A[n][k] * B[k][m] for k in range(K))
        return C
    ```

### ベクトルと行列

- ベクトルの一次変換
    - 以下の変換(平面での拡大・縮小・回転)を行うこと
        $$ A =
        \begin{pmatrix}
            x \\ y
        \end{pmatrix} \to
        A' =
        \begin{pmatrix}
            x' \\ y'
        \end{pmatrix}
        $$
    - 変換の計算式(パラメータ: $a, b, c, d$ )
        - パラメータ: $ a, b $ がx軸に影響を与える
        - パラメータ: $ c, d $ がy軸に影響を与える
        $$ \begin{alignat}{2}
        x' = ax + by \\
        y' = cx + dy
        \end{alignat} $$
        $$ \begin{pmatrix}
            x' \\ y'
        \end{pmatrix} =
        \begin{pmatrix}
            a & b \\
            c & d
        \end{pmatrix}
        \begin{pmatrix}
            x \\ y
        \end{pmatrix}$$
    - 標準基底の行き先が決まれば、すべてのベクトルの行き先が決まる
        - 平面ベクトルの点を動かすのではなく `標準規定` の $e_1, e_2$を動かして、平面全体を移動させる操作と考えることができる。
        - `標準規定` と `パラメータ` の関係
            $$ e_1 =
            \begin{pmatrix}
                a \\ c
            \end{pmatrix} \\
            e_2 =
            \begin{pmatrix}
                b \\ d
            \end{pmatrix} $$

    - 平面ベクトルの一次変換とは、 $ 2 * 2の行列A $ を `左から掛ける操作` である
    - *自分の理解*
        - 変換は変更する点を移動する考え方ではない
        - `標準規定` をずらしてから、 `標準規定` に合わせてグラフを動かすイメージ
            1. `標準規定` のベースを決める
            2. `標準規定` の移動する。(点はまだ動かない。グラフが動く)
            3. `標準規定` の移動したグラフを元の位置に戻す。(点も一緒に動かす)

- 平面ベクトル
    - $ x = 2 $, $ y = 3 $に座標を持つ点 `式(2, 3)` の平面ベクトルでの表し方
        $$ x =
        \begin{pmatrix}
            2 \\ 3
        \end{pmatrix}$$
    - 平面ベクトルは $ 2 * 1 の行列$

- 標準規定
    - $e_1$ はx軸の大きさを表す
    - $e_2$ はy軸の大きさを表す
        $$ e_1 =
        \begin{pmatrix}
            1 \\ 0
        \end{pmatrix}, e_2 =
        \begin{pmatrix}
            0 \\ 1
        \end{pmatrix}$$
        $$ \begin{pmatrix}
            x \\ y
        \end{pmatrix} = x
        \begin{pmatrix}
            1 \\ 0
        \end{pmatrix} + y
        \begin{pmatrix}
            0 \\ 1
        \end{pmatrix}$$

- 三次元の変換
    - 一次変換の式
        $$ x = x_1e_1 + x_2e_2 + x_3e_3$$
    - 選定基準
        $$ e_1 =
        \begin{pmatrix}
            1 \\ 0 \\ 0
        \end{pmatrix},
        e_2 =
        \begin{pmatrix}
            0 \\ 1 \\ 0
        \end{pmatrix},
        e_3 =
        \begin{pmatrix}
            0 \\ 0 \\ 1
        \end{pmatrix}
        $$
    - 変換行列は $ 3 * 3の正方行列$ で表現される
        $$ A =
        \begin{pmatrix}
            a_{11} & a_{12} & a_{13} \\
            a_{21} & a_{22} & a_{23} \\
            a_{31} & a_{32} & a_{33} \\
        \end{pmatrix}
        $$
        $$ e_1 =
        \begin{pmatrix}
            a_{11} \\ a_{12} \\ a_{13}
        \end{pmatrix},
        e_2 =
        \begin{pmatrix}
            a_{21} \\ a_{22} \\ a_{23}
        \end{pmatrix},
        e_3 =
        \begin{pmatrix}
            a_{31} \\ a_{32} \\ a_{33}
        \end{pmatrix}
        $$
    - 回転変換行列Aと拡大縮小行列Bの場合
        $$ x' = (BA)x $$

#### 平面ベクトルのPythonコード

- ベクトルの一次変換

    ```python
    import random

    import matplotlib.pyplot as plt

    # 45度回転行列
    A = [[1 / 1.414, -1 / 1.414], [1 / 1.414, 1 / 1.414]]

    # 2倍に拡大
    B = [[2, 0], [0, 2]]

    # 1/2倍に縮小
    C = [[0.5, 0], [0, 0.5]]

    # 90度回転行列
    D = [[1, 1], [0, 1]]


    def matmul(A, B):
        # print(f"{len(A[0])=}")
        # print(f"{len(B)=}")
        assert len(A[0]) == len(B)
        N, K, M = len(A), len(A[0]), len(B[0])
        # print(f"{N=}, {K=}, {M=}")
        C = [[0 for m in range(M)] for n in range(N)]
        # print(f"{C=}")
        for n in range(N):
            for m in range(M):
                C[n][m] = sum(A[n][k] * B[k][m] for k in range(K))
                # print(f"{C=}")
        return C


    def generate_random_points():
        points = []
        for _ in range(10):
            x1 = random.uniform(-0.6, 0.6)
            x2 = random.uniform(-0.6, 0.6)
            x = [[x1], [x2]]
            points.append(x)

        return points


    def change(points, vectors):
        new_points = []
        for x in points:
            new_points.append(matmul(vectors, x))

        for i, values in enumerate(zip(points, new_points)):
            print(f"{i=}")
            print(f"old = {values[0]}")
            print(f"new = {values[1]}")

        return new_points


    def display_result(points, new_points, vectors):
        fig = plt.figure(figsize=(10, 4))
        subplot = fig.add_subplot(1, 2, 1)
        xs = [x for x, y in points]
        ys = [y for x, y in points]
        subplot.scatter(xs, ys, color="g")
        subplot.scatter(0, 1, color="b")
        subplot.scatter(1, 0, color="r")
        subplot.set_xlim((-1, 1))
        subplot.set_ylim((-1, 1))
        subplot.hlines(0, -1, 1, color="Black", linestyles="dotted", label="")
        subplot.vlines(0, -1, 1, color="Black", linestyles="dotted", label="")
        subplot.set_aspect("equal")

        subplot = fig.add_subplot(1, 2, 2)
        xs = [x for x, y in new_points]
        ys = [y for x, y in new_points]
        subplot.scatter(xs, ys, color="g")
        subplot.scatter(vectors[0][0], vectors[0][1], color="r")
        subplot.scatter(vectors[1][0], vectors[1][1], color="b")
        subplot.set_xlim((-1, 1))
        subplot.set_ylim((-1, 1))
        subplot.hlines(0, -1, 1, color="Black", linestyles="dotted", label="")
        subplot.vlines(0, -1, 1, color="Black", linestyles="dotted", label="")
        subplot.set_aspect("equal")

        plt.show()


    def test_matmul():
        A = [[1, 2, 3], [4, 5, 6]]
        B = [[1, 2], [3, 4], [5, 6]]
        print(matmul(A, B))


    if __name__ == "__main__":
        # points = generate_random_points()
        points = [[[0.6], [0.3]]]
        new_points = change(points, A)
        display_result(points, new_points, A)

    ```

## 第4章 集合・位相
