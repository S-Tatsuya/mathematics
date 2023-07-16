def matmul(A, B):
    print(f"{len(A[0])=}")
    print(f"{len(B)=}")
    assert len(A[0]) == len(B)
    N, K, M = len(A), len(A[0]), len(B[0])
    print(f"{N=}, {K=}, {M=}")
    C = [[0 for m in range(M)] for n in range(N)]
    print(f"{C=}")
    for n in range(N):
        for m in range(M):
            C[n][m] = sum(A[n][k] * B[k][m] for k in range(K))
            print(f"{C=}")
    return C


if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[1, 2], [3, 4], [5, 6]]
    print(matmul(A, B))
