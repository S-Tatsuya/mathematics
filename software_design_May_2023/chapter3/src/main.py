import random

import matplotlib.pyplot as plt

# 45度回転行列
A = [[1 / 1.414, -1 / 1.414], [1 / 1.414, 1 / 1.414]]

# 2倍に拡大
B = [[2, 0], [0, 2]]

# 1/2倍に縮小
C = [[0.5, 0], [0, 0.5]]

# 90度回転行列
D = [[0, 1], [0, 1]]


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


def display_result(points, new_points):
    fig = plt.figure(figsize=(10, 4))
    subplot = fig.add_subplot(1, 2, 1)
    xs = [x for x, y in points]
    ys = [y for x, y in points]
    subplot.scatter(xs, ys)
    subplot.set_xlim((-2, 2))
    subplot.set_ylim((-2, 2))
    subplot.set_aspect("equal")

    subplot = fig.add_subplot(1, 2, 2)
    xs = [x for x, y in new_points]
    ys = [y for x, y in new_points]
    subplot.scatter(xs, ys)
    subplot.set_xlim((-2, 2))
    subplot.set_ylim((-2, 2))
    subplot.set_aspect("equal")

    plt.show()


def test_matmul():
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[1, 2], [3, 4], [5, 6]]
    print(matmul(A, B))


if __name__ == "__main__":
    points = generate_random_points()
    new_points = change(points, A)
    display_result(points, new_points)
