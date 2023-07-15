# Software Design ２０２３年５月号の数学特集の学習

- [Amazonリンク](https://www.amazon.co.jp/Software-Design-ソフトウェアデザイン-2023年5月号-雑誌-ebook/dp/B0C1J9BMWT/ref=sr_1_5?qid=1689412419&s=books&sr=1-5)
- 学習状況
    - [ ] 第1章 確率・統計
    - [ ] 第2章 微分・積分
    - [ ] 第3章 線形代数
    - [ ] 第4章 集合・位相

## 第1章 確率・統計

## 第2章 微分・積分

## 第３章 線形代数

- ベクトルのメリットは膨大なデータを扱う場合も同じルールで計算できる

- ベクトルの表現：
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

- Pythonではリストを使って表す

## 第4章 集合・位相
